from django.contrib import admin
from .models import Item, Request, Department

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'status', 'submitted_by', 'approved_by_principal', 'approved_by_trust')
    
class RequestAdmin(admin.ModelAdmin):
    list_display = ('item', 'status')

admin.site.register(Item, ItemAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Department)