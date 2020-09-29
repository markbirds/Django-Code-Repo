from django.urls import path
from django.views.generic import TemplateView
from .views import UserFormView, UserCreateView, UserUpdateView, UserDeleteView
from display_views.views import UserListView

app_name = 'editing_views'
urlpatterns = [
    path('', TemplateView.as_view(template_name="editing_views/index.html"),name='index'),
    path('form/', UserFormView.as_view(),name='form'),
    path('success/', TemplateView.as_view(template_name="editing_views/success.html"),name='success'),
    path('create/', UserCreateView.as_view(),name='create'),
    path('update/', UserListView.as_view(template_name="editing_views/updatelist.html"),name='updatelist'),
    path('update/<str:pk>', UserUpdateView.as_view(),name='update'),
    path('delete/', UserListView.as_view(template_name="editing_views/deletelist.html"),name='deletelist'),
    path('delete/<str:pk>', UserDeleteView.as_view(),name='delete'),
]
