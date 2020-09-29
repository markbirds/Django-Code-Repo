from django.forms import ModelForm, TextInput
from .models import NamesModel

class Names(ModelForm):
    class Meta:
        model = NamesModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name',
                'id': 'name_id',
            }),
        }