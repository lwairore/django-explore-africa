from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Category, Location, AboutMe

def home(request):
    """
        This function takes:
            1. request object as a parameter, that is by the URLconf.
        This functions retrieves all images and renders them to index.html in homepage folder.   
    """
    images = Image.objects.all()
    countries = Location.objects.all().order_by('name')
    about_me = AboutMe.objects.all()

    return render(request,'homepage/main.html', {'images':images, 'countries':countries, "about_me":about_me})
    


