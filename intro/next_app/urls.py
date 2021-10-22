from django.urls import path

from next_app import views

urlpatterns = [
    path('1/', views.hello),
    path('2/', views.hi),
    path('3/<str:param>/', views.parameters),
    path('4/', views.templates),
    path('5/<str:param>/', views.templates2),
    # konwertery ścieżki
    # str - dopasowuje dowolny niepusty napis wyłączając separator ścieżki "/", domyślny
    # int - dopasowuje inta, zwraca int
    # slug - slug string (kebab-case)
    # uuid - univerally unique identifier (aka guid - globally unique identifier)
    # 128-bit number używany do identyfikowania informacji w systemie
    # path - to co str ale z uwzlgędnieniem "/" - dopasowuje pełną ścieżkę
    path('isitmonday/', views.is_it_monday),
    path('fruit/', views.fruit),
]