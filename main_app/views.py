from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# Create your views here.

# Static Data
class Pet:
    def __init__(self, name, image, owner, bio):
        self.name=name
        self.image=image
        self.owner=owner
        self.bio=bio

# Seed Data
pets = [
    Pet("Joe", "img", "George Washington", "Joe loves going on walks and enjoys eating his dinner every night at 6 o clock."),
    Pet("Sprinkles", "img", "Lisa Siri", "Sprinkles is your friendly neighborhood cat and would rather be left outside than be stuck inside all day.")
]

class Home(TemplateView):
    # def get(self, request):
    #     return HttpResponse("MyPetPro Home")
    template_name="home.html"

class About(TemplateView):
    template_name="about.html"
    # def get(self,request):
    #     return HttpResponse("MyPetPro About")
    
class PetList(TemplateView):
    template_name="pet_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = pets
        return context