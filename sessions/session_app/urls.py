from django.urls import path
from .views import UserLogin, UserSignup
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index/index.html'),name='index'),
    path('login/',UserLogin.as_view(),name='login'),
    path('login/success',TemplateView.as_view(template_name='login/success.html'),name='success'),
    path('signup/',UserSignup.as_view(),name='signup'),
]