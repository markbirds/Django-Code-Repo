from .models import MyUUIDModel
from django.forms import ModelForm, TextInput, Textarea

class Users(ModelForm):
    class Meta:
        model = MyUUIDModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter name'
                    }),
            'description': Textarea(attrs={
                        'class': 'form-control',
                        'rows': "5"
                    }),
            }
