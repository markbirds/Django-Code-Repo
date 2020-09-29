from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import MyUUIDModel
from .forms import Users

# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    if request.method == 'POST':
        form = Users(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = Users()
    return render(request,'add.html',{'form':form})

def view(request):
    return render(request,'view.html',{'users':MyUUIDModel.objects.all()})
