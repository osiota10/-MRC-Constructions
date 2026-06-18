from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home (request):
    context = {}

    herosection = heroContent.objects.all()
    what_we_do = whatWeDo.objects.all()
    what_we_do_content =  whatWeDoContent.objects.all()
    who_we_are = WhoWeAre.objects.all()
    who_we_are_stats = WhoWeAreStats.objects.all()
    our_services = OurServices.objects.all()
    our_services_list = OurServicesList.objects.all()
    our_projects = OurProjects.objects.all()
    our_clients = OurClients.objects.all()

    context['hero-content'] = herosection
    context['what-we-do'] = what_we_do
    context['what-we-do-content'] = what_we_do_content
    context['who-we-are'] = who_we_are
    context['who-we-are-stats'] = who_we_are_stats
    context['our-services'] =  our_services
    context['our-services-list'] = our_services_list
    context['our-projects'] = our_projects
    context['our-clients'] = our_clients
    


    return render(request, 'home.html', context=context)

def services (request):
    context = {}

    servicepage = ServicePage.objects.all()
    servicecontent = ServicePageContent.objects.all()


    context['service-page'] = servicepage
    context['service-content'] = servicecontent



    return render(request, 'services.html', context=context)

def projects (request):
    context = {}
    projectpage = ProjectPage.objects.all()

    context['project-page'] = projectpage

    return render(request, 'projects.html', context=context)

def about (request):
    context = {}
    aboutpage = AboutUsPage.objects.all()
    aboutcontent = AboutUsPageContent.objects.all()
    aboutcontenttwo = AboutUsPageContentTwo.objects.all()

    context ['about-page'] = aboutpage
    context['about-content'] = aboutcontent
    context['about-content-two'] = aboutcontenttwo

    return render(request, 'about.html', context=context)

def career (request):
    context = {}

    careerpage = CareerPage.objects.all()
    careercontent = CareerPageContent.objects.all()

    context['career-page'] = careerpage
    context['career-content'] = careercontent


    return render(request, 'career.html', context=context)

def contact(request):
    context = {}

    contactpage = ContactPage.objects.all()
    contactimg = ContactPageImg.objects.all()

    context['contact-page'] = contactpage
    context['contact-page-image'] = contactimg

    


    return render(request, 'contact.html', context=context)

