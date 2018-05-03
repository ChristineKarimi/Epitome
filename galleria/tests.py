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