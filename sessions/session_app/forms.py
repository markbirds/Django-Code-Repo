from django import forms
from .models import User
from django.forms import ModelForm, TextInput, PasswordInput

class Users(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=50,
        error_messages={'required': 'Please enter your username'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        label='Age',
        error_messages={'required': 'Please enter your password'},
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter username'
                    }),
            'password': PasswordInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter password'
                    })}