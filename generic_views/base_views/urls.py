from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ViewForm,
    DeleteView,
    DeleteRecordView, 
    ReadView, 
    TemplateOne,
    TemplateTwo,
    TemplateThree,
    TemplateFour,
    )
from . import views

app_name = 'base_views'
urlpatterns = [
    path('',TemplateView.as_view(template_name='base_views/index.html'),name='index'),
    path('base/',TemplateView.as_view(template_name='base_views/base.html'),name='base'),
    path('base/add',ViewForm.as_view(),name='add'),
    path('base/read',ReadView.as_view(),name='read'),
    path('base/delete/',DeleteView.as_view(),name='delete'),
    path('base/delete/record/<str:id>',DeleteRecordView.as_view(),name='delete_record'),
    path('template/',TemplateView.as_view(template_name="base_views/template_views/index.html"),name='template_page'),
    path('template/1',TemplateOne.as_view(),name='template1'),
    path('template/2',TemplateTwo.as_view(),name='template2'),
    path('template/3',TemplateThree.as_view(),name='template3'),
    path('template/4',TemplateFour.as_view(template_number = "custom number"),name='template4'),
]