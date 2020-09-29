from django.shortcuts import render
from .models import AjaxModel
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def get(request):
    return render(request,'get.html')

def post(request):
    users = AjaxModel.objects.all()
    return render(request,'post.html',{'users':users})

def api(request):
    if request.method == 'GET':
        users = AjaxModel.objects.all()
        data = serializers.serialize("json", users)
        return JsonResponse(data,safe=False)
    else:
        user = AjaxModel.objects.get(id=request.POST.get('id'))
        data = {
            "name": user.name,
            "id": user.id,
            "age": user.age
        }
        return JsonResponse(data,safe=False)



