from django.shortcuts import render
from .models import Image

# Create your views here.
def gallery(request):
    all_pics = Image.all_pics()
    return render(request, 'gallery.html', {"all_pics":all_pics})