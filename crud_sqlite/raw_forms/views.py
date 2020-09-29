from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from datetime import datetime
from .models import RawForm

# Create your views here.
def index(request):
    return render(request,'raw_forms/index.html')

def create(request):
    if request.method == 'POST':
        likes_programming = False
        if request.POST.get('fave_programming') =='on':
            likes_programming = True
        RawForm.objects.create(
            name = request.POST.get('name', False),
            age = request.POST.get('age'),
            email = request.POST.get('email'),
            birthday = request.POST.get('birthday'),
            language = request.POST.get('fave_programming'),
            programmer = likes_programming
        )
        return HttpResponseRedirect(reverse('raw_forms:create'))
    return render(request,'raw_forms/create.html')

def read(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'raw_forms/read.html',context)

def read_details(request,id):
    objects = RawForm.objects.get(id=id)
    context = {
        "record": objects
    }
    return render(request,'raw_forms/read_details.html',context)

def update(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'raw_forms/update.html',context)

def update_form(request,id):
    if request.method == 'POST':
        likes_programming = False
        if request.POST.get('likes_programming') =='on':
            likes_programming = True
        record = RawForm.objects.get(id=id)
        record.name = request.POST.get('name', False)
        record.age = request.POST.get('age')
        record.email = request.POST.get('email')
        record.birthday = request.POST.get('birthday')
        record.language = request.POST.get('fave_programming')
        record.programmer = likes_programming
        record.save()
        return HttpResponseRedirect(reverse('raw_forms:update'))
    objects = RawForm.objects.get(id=id)
    context = {
        "record": objects,
        "birthday": objects.birthday.strftime('%Y-%m-%d')
    }
    return render(request,'raw_forms/update_form.html',context)

def delete(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'raw_forms/delete.html',context)

def delete_record(request,id):
    record = RawForm.objects.get(id=id)
    record.delete()
    return redirect('raw_forms:index')


