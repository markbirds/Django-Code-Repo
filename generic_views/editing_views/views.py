from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import Users
from display_views.models import DisplayViewModel
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# Create your views here.

class UserFormView(FormView):
    template_name = 'editing_views/formview.html'
    form_class = Users
    success_url = '/display_views/detail/'

    def form_valid(self, form):
        DisplayViewModel.objects.create(
            name=form.cleaned_data.get('name'),
            age=form.cleaned_data.get('age')
            )
        return super().form_valid(form)

class UserCreateView(CreateView):
    template_name = 'editing_views/createview.html'
    form_class = Users
    success_url = '/editing_views/'

class UserUpdateView(UpdateView):
    template_name = 'editing_views/updateview.html'
    form_class = Users
    success_url = '/editing_views/update/'
    queryset = DisplayViewModel.objects.all()

class UserDeleteView(DeleteView):
    template_name = 'editing_views/deleteview.html'
    success_url = reverse_lazy('editing_views:deletelist')
    queryset = DisplayViewModel.objects.all()