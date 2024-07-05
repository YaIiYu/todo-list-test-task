from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/<str:status>/', views.complete, name='complete'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('remove/<int:task_id>/', views.remove, name='remove'),
    path('tags/', views.tag_list, name='tag_list'),
]
