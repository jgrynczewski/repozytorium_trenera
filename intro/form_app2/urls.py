from django.urls import path

from . import views

app_name = 'form2'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('list/', views.tasks_list, name='list'),
]