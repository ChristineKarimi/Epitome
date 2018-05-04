from django.shortcuts import render
from .models import Image

# Create your views here.
def galleria(request):
    all_pics = Image.all_pics()
    return render(request, 'galleria.html', {"all_pics":all_pics})

def display_images_categories(request):    
    pics = Image.pic_categories()

    return render(request, 'categories.html', {"pics":pics}) 
