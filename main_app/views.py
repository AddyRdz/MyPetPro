from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Pet
# Create your views here.

# Static Data
# class Pet:
#     def __init__(self, name, image, owner, bio):
#         self.name=name
#         self.image=image
#         self.owner=owner
#         self.bio=bio

# Seed Data
# pets = [
#     Pet("Joe", "img", "George Washington", "Joe loves going on walks and enjoys eating his dinner every night at 6 o clock."),
#     Pet("Sprinkles", "img", "Lisa Siri", "Sprinkles is your friendly neighborhood cat and would rather be left outside than be stuck inside all day.")
# ]

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
        # This information will be used once I have added a search function to my pet_list 3/1 pm :30min
        # name = self.request.GET.get("name")
        # print(name)
        # if name != None:
        #     context['pets'] = Pet.object.filter(name_icontains=name)
        #     context['header'] =f"Results for: {name}"
        # else:
        #     context['pets'] = Pet.objects.all()
        #     context['header'] = 'Pets'
        # return context



        context['pets'] = Pet.objects.all()
        return context

class PetCreate(CreateView):
    model = Pet
    fields = ['name', 'img', 'owner', 'bio']
    template_name = 'pet_create.html'
    success_url = '/pet/'

class PetDetail(DetailView):
    model = Pet
    template_name = "pet_detail.html"