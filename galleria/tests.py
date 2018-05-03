from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.blackish = Image(name = 'blackish', description = 'blackish poster')
        self.blackish.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.blackish, Image))


    def test_save_method(self):
        self.blackish.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 


    def test_delete_method(self):
        self.new_image = Image(name = 'flower', description = 'the beauty of a roseflower despite its thorns')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)


    def test_update_method(self):
        self.vic = Image(name = 'danvictor', description = 'an image of victor')
        self.vic.save_image()
        self.vic = Image(name = 'danvic', description = 'an image of victor')        
        self.vic.update_image(name = 'danvic')
        self.vic.save_image()
        images = Image.objects.filter(name = 'danvic')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class CategoryTestClass(TestCase):
    def setUp(self):
        self.nature = Category(name = 'nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.nature, Category))

    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)        

    def test_delete_method(self):
        self.new_category = Category(name = 'autumn')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)   

    def test_update_category(self):
        self.health = Category(name = 'Food')
        self.health.save_category()
        self.health = Category(name = 'Fashion')
        self.health.save_category()
        self.health.update_category(name = 'Nature')
        categories = Category.objects.filter(name = 'People')
        self.assertEqual(len(categories), 1)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

class LocationTestClass(TestCase):    
    def setUp(self):
        self.Kenya = Location(name = 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya, Location))

    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
