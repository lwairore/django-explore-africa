from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Category, Location
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    images = Image.objects.all()
    locations = []
    locations_all = Location.objects.all()
    
    for i in locations_all:
        if i.name not in locations:
            locations.append(i.name)
    print(locations)
            
    return render(request,'homepage/index.html', {'images':images, 'locations':locations})
    
def search_results(request):
    if 'category' in request.GET and request.GET['category']:
            try: 
                search_term = request.GET.get('category') 
                print(Category.objects.all())
                category = Category.objects.filter(name=search_term)
                print('Primary key',category)
                print(search_term)
            
                category_all = Category.objects.all()
            

                images_final = []
                for i in category_all:
                    if search_term == i.name:
                        print(i.id)
                        searched_images = Image.search_image(i.id)
                        images_final.append(searched_images)
                        print(searched_images)
                        print(images_final)
                message = f'{search_term}'
                return render(request, 'search/search_results.html', {'message':message, 'searched_images':searched_images, 'images_final':images_final })

            except:
                raise Http404()
                    
    else: 
        message = 'You haven\'t searchded for any term'
        return render(request, 'search/search_results.html', {'message':message})

