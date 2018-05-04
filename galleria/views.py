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

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})