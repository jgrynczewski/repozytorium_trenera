from django.urls import path

from auth_sys import views

app_name = "auth"

urlpatterns = [
    path('cookies/', views.cookies, name="cookies"),
    path('session/', views.session, name="session"),
]