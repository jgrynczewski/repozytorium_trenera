from django.urls import path

from api import views

app_name='api'

urlpatterns = [
    path('fixer/', views.fixer, name='fixer'),
    path('goodreads/', views.goodreads, name='goodreads'),
]