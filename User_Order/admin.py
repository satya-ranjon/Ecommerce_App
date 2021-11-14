from django.contrib import admin
from .models import Oreder,Cart
# Register your models here.

# admin.site.register(Oreder)
@admin.register(Cart)
class Cart(admin.ModelAdmin):
    '''Admin View for Post'''
    list_display = (
        'user',
        'item',
        'quantity',
        'purchased',
        'created_date',
        'updated_date',
    )
    fieldsets = (
        (None, {
            "fields": (
                'user',
                'item',
                'quantity',
                'purchased',
            ),
        }),
    )
    list_filter = (
        'purchased',
    )
    
    
@admin.register(Oreder)
class Oreder(admin.ModelAdmin):
    '''Admin View for Post'''
    list_filter = (
        'ordered',
    )
    list_display = (
            'user',
            'ordered',
            'paymentId',
            'orderId',
            'created_date',
    )
    fieldsets = (
        (None, {
            "fields": (
                'orderitems',
                'user',
                'ordered',
                'paymentId',
                'orderId',
            ),
        }),
    )





