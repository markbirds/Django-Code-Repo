from django.urls import path
from django.views.generic import TemplateView
from .views import UserListView, DetailListView

app_name = 'display_views'
urlpatterns = [
    path('',TemplateView.as_view(template_name='display_views/index.html'),name='index'),
    path('list/',UserListView.as_view(),name='list'),
    path('detail/',UserListView.as_view(template_name="display_views/display_detail.html"),name='detail'),
    path('detail/<str:pk>',DetailListView.as_view(),name='detail_view'),

]