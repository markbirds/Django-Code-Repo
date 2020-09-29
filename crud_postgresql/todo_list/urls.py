from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/add_user/', views.add_user, name='add_user'),
    path('create/add_task/', views.add_task, name='add_task'),
    path('read/', views.read, name='read'),
    path('read_tasks/<int:id>', views.read_tasks, name='read_tasks'),
    path('update/', views.update, name='update'),
    path('update/tasks/<int:id>', views.update_task, name='update_task'),
    path('update_user/<int:id>', views.update_user_form, name='update_user_form'),
    path('update/tasks/<int:user_id>/form/<int:task_id>', views.update_task_form, name='update_task_form'),
    path('delete/', views.delete, name='delete'),
    path('delete/<int:id>', views.delete_user, name='delete_user'),
    path('delete/tasks/<int:id>', views.delete_tasks, name='delete_tasks'),
    path('delete/tasks/confirm/<int:id>', views.delete_confirm, name='delete_confirm'),
]