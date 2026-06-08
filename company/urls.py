from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
    path('career/', career, name='career'),
    path('contact/', contact, name='contact'),
]
