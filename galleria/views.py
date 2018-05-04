from django.shortcuts import render
from .models import Image

# Create your views here.
def galleria(request):
    all_pics = Image.all_pics()
    return render(request, 'galleria.html', {"all_pics":all_pics})

def display_images_categories(request):    
    pics = Image.pic_categories()

    return render(request, 'categories.html', {"pics":pics}) 


def display_images_locations(request):    
    pics = Image.pic_locations()

    return render(request, 'locations.html', {"pics":pics}) 

def single_pic(request, image_id):
    image = Image.get_pic(image_id)
    return render(request, 'single_pic.html', {"image":image})