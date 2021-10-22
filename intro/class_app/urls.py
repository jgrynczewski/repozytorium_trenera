from django.urls import path

from class_app import views

app_name = 'class_app'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    path('person/<int:id>/', views.person_detail, name='person_detail'),
    path('person2/<int:id>/', views.PersonView.as_view(), name='person_detail2'),
    # Uwaga! Tutaj musi być pk (ew. slug), a nie id.
    path('person3/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail3'),
    path('create-person/', views.create_person, name='create_person'),
    path('create-person2/', views.PersonCreateView.as_view(), name='person_view'),
    path('create-person3/', views.PersonCreateView2.as_view(), name='create_person_view')

]