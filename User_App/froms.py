from django.forms import ModelForm
from .models import User,Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm




#froms 
class ProfileForm(ModelForm):
    username = forms.CharField( label='', widget=forms.TextInput(attrs={
        'placeholder': ' Username'
    }))
    full_name = forms.CharField( label='', widget=forms.TextInput(attrs={
        'placeholder': ' Full Name'
    }))
    address_1 = forms.CharField( label='', widget=forms.Textarea(attrs={
        'placeholder': ' Current Addres',
        'rows': '4px'
    }))
    zipcode = forms.CharField( label='', required=False, widget=forms.TextInput(attrs={
        'placeholder': ' Zip Code'
    }))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': ' 01XXXXXXXXX',
        'maxlength':"11",'size':'11',
        'type':'number',
        'oninput':"javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
    }))

    def clean(self):
        all_clean_data = super().clean()
        user_phone = all_clean_data['phone']
        if len(user_phone) != 11 :
            raise forms.ValidationError('আপনার ফোন নম্বর খুব ছোট')
    
    class Meta:
        model = Profile
        exclude = ('user',)


class SingUpForm(UserCreationForm):
    email = forms.CharField( label='', widget=forms.TextInput(attrs={
        'placeholder': ' email'
    }))
    password1 = forms.CharField( label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' Password',
        'id':'myinput1',
    }))
    password2 = forms.CharField( label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' Confirm Password',
        'id':'myinput1',
    }))
    class Meta:
        model = User
        fields = ('email','password1','password2')



class LoginForm(AuthenticationForm):
    
    username = forms.CharField( label='', widget=forms.TextInput(attrs={
        'placeholder': ' email'
    }))
    password = forms.CharField( label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' Password',
        'id':'myinput1',
    }))
    class Meta:
        model = User
        fields = ('username','password',)


class ChangeUsPassword(PasswordChangeForm):

    old_password = forms.CharField( label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' Old Password',
        'id':'myinput1',
    }))
    new_password1 = forms.CharField( label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' New Password',
        'id':'myinput1',
    }))
    new_password2 = forms.CharField( label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' Confirm Password',
        'id':'myinput1',
    }))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)