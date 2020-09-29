from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('',views.usersList,name='userList'),
    path('create/',views.usersCreate,name='usersCreate'),
    path('get/<str:id>',views.getUser,name='getUser'),
    path('update/<str:id>',views.updateUser,name='updateUser'),
    path('delete/<str:id>',views.deleteUser,name='deleteUser'),
]