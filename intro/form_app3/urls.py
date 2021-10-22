from django.urls import path

from . import views

app_name = 'form3'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('task_list/', views.task_list, name='task_list'),
]