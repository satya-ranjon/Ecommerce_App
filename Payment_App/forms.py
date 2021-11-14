from django import forms
from django.forms import fields
from .models import BillingAddress


class BillingForm(forms.ModelForm):
    country = forms.CharField( label=' Your Country', widget=forms.TextInput(attrs={
        'placeholder': ' Country'
    }))
    city = forms.CharField( label=' Your City ', widget=forms.TextInput(attrs={
        'placeholder': ' City'
    }))
    address = forms.CharField( label=' Current Address', widget=forms.TextInput(attrs={
        'placeholder': ' Current Addres',
    }))
    zipcode = forms.CharField( label=' Zip Code', widget=forms.NumberInput(attrs={
        'placeholder': ' Zip Code'
    }))
    class Meta:
        model = BillingAddress
        fields = ('address','zipcode','city','country',)