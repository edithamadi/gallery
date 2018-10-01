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

   def test_update_method(self):
       """
       Function to test that an image's details can be updates
       """
       self.image.save_image()
       new_image = Image.objects.filter(image='test.jpg').update(image='pic.jpg')
       images = Image.objects.get(image='pic.jpg')
       self.assertTrue(images.image, 'pic.jpg')

   def test_get_image_by_id(self):
       """
       Function to test if you can get an image by its id
       """
       self.image.save_image()
       this_img= self.image.get_image_by_id(self.image.id)
       image = Image.objects.get(id=self.image.id)
       self.assertTrue(this_img, image)

#    def test_search_image(self):
#         """
#         Function to test if you can search an image
#         """
#         self.image.save_image()
#         images = Image.search_image('waterfalls')
#         self.assertTrue(len(images)>0)

#    def test_filter_by_location(self):
#        """
#        Function to test if you can get an image by its location
#        """
#        self.image.save_image()
#        this_img = Image.search_by_location('nairobi')
#        image = Image.objects.filter(location=self.image.location_id)
#        self.assertTrue(this_img, image)

#    def test_filter_by_Category_name(self):
#        """
#        Function to test if you can get an image by its Category name
#        """
#        self.image.save_image()
#        images = Image.search_image(self.image)
#        self.assertTrue(len(images)>0)

# #    def test_get_all_images(self):

#        """
#        Function to test if you can get all images
#        """
#        self.image.save_image()
#        self.assertTrue(len(images)>0)

