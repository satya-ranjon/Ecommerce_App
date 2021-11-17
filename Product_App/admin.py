from django.contrib import admin
from .models import Products,Catagory
# Register your models here.
# admin.site.register(Products)
admin.site.register(Catagory)



@admin.register(Products)
class Products(admin.ModelAdmin):
    '''Admin View for Post'''
    search_fields =('name',)
    list_filter = (
            'catagory',
    )
    list_display = (
        'name',
        'catagory',
        'price',
        'old_price',
    )
    fieldsets = (
        (None, {
            "fields": (
                'minimage',
                'more_img',
                'img1',
                'img2',
                'img3',
                'name',
                'catagory',
                'preview_text',
                'detail_text',
                'price',
                'old_price',
            ),
        }),
    )