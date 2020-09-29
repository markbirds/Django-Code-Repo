from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('api/', views.api, name='api'),
]
