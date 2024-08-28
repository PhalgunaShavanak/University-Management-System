from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ItemForm  # Import ItemForm
from .models import Item  # Import Item model
from django.contrib import messages  # Import messages framework

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == 'Phalguna':
                return redirect('admin:index')  # Redirect to admin dashboard
            elif user.username == 'AIML':
                return redirect('hod_dashboard')
            elif user.username == 'Principal':
                return redirect('principal_dashboard')
            elif user.username == 'Trust':
                return redirect('trust_dashboard')
        else:
            return render(request, 'gst_app/login.html', {'error': 'Invalid username or password'})
    return render(request, 'gst_app/login.html')

@login_required
def hod_dashboard(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            quantity = form.cleaned_data['quantity']
            # Save the item and quantity to the database
            Item.objects.create(item_name=item_name, quantity=quantity, submitted_by=request.user)
            return render(request, 'gst_app/hod_dashboard.html', {'form': form, 'message': 'Successfully submitted'})
    else:
        form = ItemForm()

    return render(request, 'gst_app/hod_dashboard.html', {'form': form})

@login_required
def principal_dashboard(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        action = request.POST.get('action')
        
        try:
            item = Item.objects.get(id=item_id)
            if action == 'approve':
                item.approved_by_principal = True
                item.status = 'Approved'
                messages.success(request, 'Item successfully approved.')
            elif action == 'disapprove':
                item.approved_by_principal = False
                item.status = 'Disapproved'
                messages.error(request, 'Item successfully disapproved.')
            item.save()
        except Item.DoesNotExist:
            messages.error(request, 'Item does not exist.')

        return redirect('principal_dashboard')
    
    items = Item.objects.all()
    return render(request, 'gst_app/principal_dashboard.html', {'items': items})

def trust_dashboard(request):
    # Filter items that are approved by the principal
    items = Item.objects.filter(status='Approved')
    return render(request, 'gst_app/trust_dashboard.html', {'items': items})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'gst_app/home.html')