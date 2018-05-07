from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url



urlpatterns=[
   url(r'^$', views.gallery, name = 'gallery'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^categories/', views.display_images_categories, name = 'categories'),
    url(r'^locations/', views.display_images_locations, name = 'locations'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)