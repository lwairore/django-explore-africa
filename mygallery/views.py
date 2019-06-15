from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.

def home(request):
    images = Image.objects.all()
    return render(request,'homepage/index.html', {'images':images})
    