from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# Create your views here.

class Home(TemplateView):
    # def get(self, request):
    #     return HttpResponse("MyPetPro Home")
    template_name="home.html"

class About(TemplateView):
    template_name="about.html"
    # def get(self,request):
    #     return HttpResponse("MyPetPro About")
    