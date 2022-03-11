from django.db import models
from django.forms import ModelForm


# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class PetForm(ModelForm):
    class Meta:
        model=Pet
        fields= ['name', 'img', 'owner', 'bio']

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

# class Vaccine(models.Model):
#     vaccine_type = ( 
#         ('Rabies', 'Rabies'),
#         ('DHPP', 'DHPP'),
#         ('Bordetella', 'Bordetella'),
#         ('Leptospirosis', 'Leptospirosis'),
#         ('Canine Influenza', 'Canine Influenza'),

#     )

#     vaccine = models.ForeignKey(Health,on_delete=models.CASCADE)
