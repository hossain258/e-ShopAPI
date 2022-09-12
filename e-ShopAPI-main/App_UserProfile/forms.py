from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name =forms.CharField(max_length=200)
    phone =forms.CharField(max_length=13)
    addressline1 = forms.CharField (max_length=200,required=True)
    addressline2 = forms.CharField (max_length=200,required=True)
    city = forms.CharField (max_length=200,required=True)
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError('Email Already Exists')
    #     return email
    class Meta:
        model = User
        fields = ['username', 'email','name','phone','addressline1','addressline2','city', 'password1', 'password2']