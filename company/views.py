from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home (request):
    


    return render(request, 'home.html')

def services (request):
    


    return render(request, 'services.html')

def projects (request):
    


    return render(request, 'projects.html')

def about (request):
    


    return render(request, 'about.html')

def career (request):
    


    return render(request, 'career.html')

def contact(request):
    


    return render(request, 'contact.html')

