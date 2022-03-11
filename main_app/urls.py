from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('pet/', views.PetList.as_view(), name="pet_list"),
    path('pet/new/', views.PetCreate.as_view(), name="pet_create"),
    path('pet/<int:pk>/', views.PetDetail.as_view(), name="pet_detail"),
    path('pet/<int:pk>/update', views.PetUpdate.as_view(), name="pet_update"),
    path('pet/<int:pk>/delete', views.PetDelete.as_view(), name="pet_delete"),
    path('pet/<int:pk>/health/new', views.HealthCreate.as_view(), name="health_create")
    # path('pet/<int:pk>/health/update', views.HealthUpdate.as_view(), name="health_update")
]


    