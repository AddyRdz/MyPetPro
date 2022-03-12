from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import HealthForm, Pet, Health, PetForm, HealthForm
from django.shortcuts import redirect

# Create your views here.

# Static Data
# class Pet:
#     def __init__(self, name, image, owner, bio):
#         self.name=name
#         self.image=image
#         self.owner=owner
#         self.bio=bio

# Seed Data
# healths = [
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
        
        name = self.request.GET.get("name")
        print(name)
        if name != None:
            context['pets'] = Pet.objects.filter(name__icontains=name)
            context['header'] =f"Results for: {name}"
        else:
            context['pets'] = Pet.objects.all()
            context['header'] = 'Pets'
        return context



class PetCreate(View):
    def post(self, request):
        print ("test,hello")
        
        name = request.POST.get("name")
        img = request.POST.get("img")
        owner = request.POST.get("owner")
        bio = request.POST.get("bio")
        new_pet=Pet.objects.create(name=name, img=img, owner=owner, bio=bio) 
        Health.objects.create(pet=new_pet)
        
        return redirect ("pet_list")
        
    def get(self,request):
            form=PetForm()
            context={"form": form} 
            return render(request, "pet_create.html", context)
               
        
    
    # model = Pet
    # fields = ['name', 'img', 'owner', 'bio']
    # template_name = 'pet_create.html'
    # success_url = '/pet/'


class PetDetail(DetailView):
    model = Pet
    template_name = "pet_detail.html"

class PetUpdate(UpdateView):
    model = Pet
    fields = ['name', 'img', 'owner', 'bio']
    template_name = 'pet_update.html'
    success_url = '/pet/'

class PetDelete(DeleteView):
    model = Pet
    template_name = "pet_delete_confirmation.html"
    success_url = '/pet/'

class HealthCreate(View):
    def post(self, request, healthpk, petpk):
        food = request.POST.get("food")
        health_issues = request.POST.get("health_issues")
        weight = request.POST.get("weight")
        rabies = True if request.POST.get("rabies") == "on" else False
        dhpp =  True if request.POST.get("dhpp") == "on" else False
        bordetella = True if request.POST.get("bordetella") == "on" else False
        lepto =  True if request.POST.get("lepto") == "on" else False
        canine_flu = True if request.POST.get("canine_flu") == "on" else False
        pet = Pet.objects.get(pk=petpk)
        Health.objects.update(food=food, health_issues=health_issues, weight=weight, rabies=rabies, dhpp=dhpp, bordetella=bordetella, lepto=lepto, canine_flu=canine_flu)
        return redirect('pet_detail',petpk)

    def get(self,request, petpk, healthpk):
        print('whats up')
        form=HealthForm()
        context={"form": form} 
        return render(request, "health_create.html", context)


