from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class PetForm(ModelForm):
    class Meta:
        model=Pet
        fields= ['name', 'img', 'owner', 'bio', 'user']

class Health(models.Model):
    pet = models.OneToOneField(Pet,on_delete=models.CASCADE, related_name="pets")
    food = models.CharField(max_length=150)
    health_issues = models.TextField(max_length=500)
    weight = models.IntegerField(default=0)
    rabies = models.BooleanField(default=False)
    dhpp = models.BooleanField(default=False)
    bordetella = models.BooleanField(default=False)
    lepto= models.BooleanField(default=False)
    canine_flu = models.BooleanField(default=False)

    def __str__(self):
        return self.pet.name

class HealthForm(ModelForm):
    class Meta:
        model=Health
        fields = [ 'food', 'health_issues', 'weight', 'rabies', 'dhpp', 'bordetella', 'lepto', 'canine_flu']





