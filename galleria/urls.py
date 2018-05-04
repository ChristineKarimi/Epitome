from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url



urlpatterns=[
   url('', views.galleria, name = 'galleria'),
   # url('search/', views.search_results, name = 'search_results'),
   # url('categories/', views.display_images_categories, name = 'categories'),
   # url('locations/', views.display_images_locations, name = 'locations'),
  #  url('image/<int:image_id>', views.single_pic, name = 'single_pic')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)