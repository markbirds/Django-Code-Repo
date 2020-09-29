from django.urls import path
from . import views

app_name = 'raw_forms'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    path('read/<int:id>',views.read_details,name='read_details'),
    path('update/',views.update,name='update'),
    path('update_form/<int:id>',views.update_form,name='update_form'),
    path('delete/',views.delete,name='delete'),
    path('delete_record/<int:id>',views.delete_record,name='delete_record'),
]