from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput, CheckboxInput
from raw_forms.models import RawForm
from django.utils.translation import gettext_lazy as _

class DjangoModelForm(ModelForm):
    class Meta:
        model = RawForm
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
            'email': EmailInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter email'
                    }),
            'birthday': DateInput(attrs={
                        'type':'date',
                        'class': 'form-control',
                        'required': True
                    }),
            'language': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter your favorite programming language'
                    }),
            'programmer': CheckboxInput(attrs={
                        'class': 'custom-control-input',
                        'placeholder': 'Enter your favorite programming language'
                    })
            }
        error_messages = {
            'email': {
                'unique': _("This email already exists."),
            }
        }

        