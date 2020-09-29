from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import DisplayViewModel

# Create your views here.

class UserListView(ListView):
    model = DisplayViewModel

class DetailListView(DetailView):
    model = DisplayViewModel


