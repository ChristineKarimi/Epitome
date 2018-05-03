from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.blackish = Image(name = 'blackish', description = 'blackish poster')
        self.blackish.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.blackish, Image))


