from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from datetime import datetime
from raw_forms.models import RawForm
from .forms import DjangoForm

# Create your views here.
def index(request):
    return render(request,'django_forms/index.html')

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DjangoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            likes_programming = False
            if form.cleaned_data['programmer'] =='on':
                likes_programming = True
            RawForm.objects.create(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age'],
                email = form.cleaned_data['email'],
                birthday = form.cleaned_data['birthday'],
                language = form.cleaned_data['language'],
                programmer = likes_programming
            )
            return HttpResponseRedirect(reverse('django_forms:create'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DjangoForm()
    return render(request,'django_forms/create.html',{'form': form})

def read(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'django_forms/read.html',context)

def read_details(request,id):
    objects = RawForm.objects.get(id=id)
    context = {
        "record": objects
    }
    return render(request,'django_forms/read_details.html',context)

def update(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'django_forms/update.html',context)

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
    return render(request,'django_forms/update_form.html',context)

def delete(request):
    objects = RawForm.objects.all()
    context = {
        "forms": objects
    }
    return render(request,'django_forms/delete.html',context)

def delete_record(request,id):
    record = RawForm.objects.get(id=id)
    record.delete()
    return redirect('django_forms:index')


