from display_views.models import DisplayViewModel
from django.forms import ModelForm, TextInput, NumberInput

class Users(ModelForm):
    class Meta:
        model = DisplayViewModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter name'
                    }),
            'age': NumberInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter age'
                    }),
            }
