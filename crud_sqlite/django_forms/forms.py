from django import forms

class DjangoForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        error_messages={'required': 'Please enter your name'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name'
        })
    )
    age = forms.IntegerField(
        label='Age',
        error_messages={'required': 'Please enter your age'},
        max_value=120,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter age'
        })
    )

    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email'
        })
    )
    birthday = forms.DateField(
        label='Birthday',
        widget=forms.DateInput(attrs={
        'type':'date',
        'class': 'form-control',
        'required': True
        })
    )
    language = forms.CharField(
        label='Favorite Programming Language',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your favorite programming language'
        })
        )
    programmer = forms.BooleanField(
        label='Likes Programming or not?',
        widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'placeholder': 'Enter your favorite programming language'
        }),
        required=False
    )

