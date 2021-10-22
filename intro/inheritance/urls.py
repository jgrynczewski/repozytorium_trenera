from django.urls import path

from inheritance import views

# Tu na koniec dorabiamy przekierowanie analogicznie
# jak w przykładzie links i zwracamy uwagę na kolizję.
# Dorabiamy name_app.

app_name = 'inheritance'

urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second')
]