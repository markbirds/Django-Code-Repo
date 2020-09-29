from django.shortcuts import render
from api.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request,'index.html',{'users':users})
