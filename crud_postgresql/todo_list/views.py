from django.shortcuts import render
from .models import User, Task
from .forms import UserForm, TaskForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'todo_list/index.html')

def create(request):
    return render(request,'todo_list/create.html')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list:create'))
    else:
        form = UserForm()
    return render(request,'todo_list/add_user.html',{'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list:create'))
    else:
        form = TaskForm()
    return render(request,'todo_list/add_task.html',{'form': form}) 

def read(request):
    users = User.objects.all().order_by('pub_date')
    return render(request,'todo_list/read.html',{'users':users})

def read_tasks(request,id):
    user = User.objects.get(id=id)
    tasks = user.task_set.all()
    return render(request,'todo_list/read_tasks.html',{'tasks':tasks})

def update(request):
    users = User.objects.all().order_by('pub_date')
    return render(request,'todo_list/update.html',{'users':users})

def update_task(request,id):
    user = User.objects.get(id=id)
    user_tasks = user.task_set.all()
    return render(request,'todo_list/update_task.html',{'user_tasks':user_tasks,'user_id':id})

def update_user_form(request,id):
    users = User.objects.get(id=id)
    form = UserForm(instance=users)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=users)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list:update'))
    return render(request,'todo_list/update_user_form.html',{'form':form})

def update_task_form(request,user_id,task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list:update_task',args=[user_id]))
    return render(request,'todo_list/update_task_form.html',{'form':form,'user_id':user_id})

def delete(request):
    users = User.objects.all().order_by('pub_date')
    return render(request,'todo_list/delete.html',{'users':users})

def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('todo_list:index'))

def delete_tasks(request,id):
    user = User.objects.get(id=id)
    user_tasks = user.task_set.all()
    return render(request,'todo_list/delete_task.html',{'user_tasks':user_tasks})

def delete_confirm(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('todo_list:delete'))