from django.urls import path

from hello_app import views

urlpatterns = [
    path('', views.hello),
    path('dwa/', views.hello2),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('isitnewyear/', views.new_year),
    path('name/<name>', views.name2),
    path('<str:name>', views.name),
]