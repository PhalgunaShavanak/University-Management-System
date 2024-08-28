from django import forms
from .models import Item

class ItemForm(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=100)
    quantity = forms.IntegerField(label='Quantity')
