from django.test import TestCase
from .models import Image,category,Location
# Create your tests here.

class CategoryTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.waterfalls= category(name = 'Waterfalls')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.waterfalls,category))

    # Testing Save Method
    def test_save_method(self):
        self.waterfalls.save_category()
        categories = category.objects.all()
        self.assertTrue(len(categories) > 0)

class LocationTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.nairobi= Location(name = 'nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestClass(TestCase):
   """
   Tests Image class and its functions
   """
   #Set up method
   def setUp(self):
       #creating a new location and saving it
       self.nairobi = Location(name='nairobi')
       self.nairobi.save_location()

       #creating a new Category and saving it
       waterfalls = category(name='waterfalls')
       waterfalls.save()

       #creating an new image
       self.image = Image(id=1,image='test.jpg', name='name', description = 'testing image class', location=self.nairobi)

   def test_instance(self):
       self.assertTrue(isinstance(self.image, Image))

   def test_save_method(self):
       """
       Function to test an image and its details is being saved
       """
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

   def test_delete_method(self):
       """
       Function to test if an image can be deleted
       """
       self.image.save_image()
       self.image.delete_image()

