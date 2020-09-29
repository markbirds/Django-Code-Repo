from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.views import View
from .forms import Users, SignupForm
from .models import User

# Create your views here.
class UserLogin(View):
    def get(self,request):
        form = Users()
        if 'username' in request.session:
            del request.session['username']
        return render(request,'login/login.html',{'form':form})
    def post(self,request):
        form = Users(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
                if user.password == form.cleaned_data['password']:
                    request.session['username'] = user.username
                    return render(request,'login/success.html')
                else:
                    return HttpResponse('Account not found')
            except:
                return HttpResponse('Account not found')
        return render(request,'login/login.html',{'form':form})


class UserSignup(CreateView):
    template_name = 'signup/signup.html'
    form_class = SignupForm
    success_url = '/'
