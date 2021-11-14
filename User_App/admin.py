from django.contrib import admin
from .models import User,Profile
# Register your models here.

admin.site.register(User)
@admin.register(Profile)
class Profile_admin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'user','username','full_name','address_1','city','zipcode','country','phone'
            ),
        }),
    )
    list_display = (
        'user','username','full_name','country','phone','zipcode','city',
    )
    search_fields =(
        'username','full_name'
    )
    list_display_links=(
        'user','username','full_name','country','phone','zipcode','city',
    )
    list_filter = (
        'city',
        'country',
    )