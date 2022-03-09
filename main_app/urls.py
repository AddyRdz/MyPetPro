from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('pet/', views.PetList.as_view(), name="pet_list"),
    path('pet/new/', views.PetCreate.as_view(), name="pet_create")
]