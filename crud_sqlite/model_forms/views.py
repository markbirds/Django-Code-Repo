from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from datetime import datetime
from raw_forms.models import RawForm
from .forms import DjangoModelForm

# Create your views here.
def index(request):
    return render(request,'model_forms/index.html')

def create(request):
    if request.method == 'POST':
        form = DjangoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('model_forms:create'))
    else:
        form = DjangoModelForm()
    return render(request,'model_forms/create.html',{'form': form})

def read(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'model_forms/read.html',context)

def read_details(request,id):
    objects = RawForm.objects.get(id=id)
    context = {
        "record": objects
    }
    return render(request,'model_forms/read_details.html',context)

def update(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'model_forms/update.html',context)

def update_form(request,id):
    record = RawForm.objects.get(id=id)
    form = DjangoModelForm(instance=record)
    if request.method == 'POST':
        form = DjangoModelForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('model_forms:update'))
    return render(request,'model_forms/update_form.html',{"form": form})

def delete(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'model_forms/delete.html',context)

def delete_record(request,id):
    record = RawForm.objects.get(id=id)
    record.delete()
    return redirect('model_forms:index')


