from django.forms import ModelForm, TextInput, Select
from .models import User, Task

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'user': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter name'
                    }),
            'gender': Select(attrs={
                        'class': 'custom-select',
                    }),
            }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'user_name': Select(attrs={
                        'class': 'custom-select',
                    }),
            'tasks': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter task'
                    }),
            }

        