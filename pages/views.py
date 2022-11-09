from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class homepage(TemplateView):
    template_name = "home.html"
    
class aboutpage(TemplateView):
    template_name = "about.html"
