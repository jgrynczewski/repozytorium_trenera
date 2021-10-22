from django.urls import path

from . import views

app_name = 'form1'

urlpatterns = [
    path('', views.register_task),
]