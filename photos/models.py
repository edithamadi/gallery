from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()
    

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_Location(self):
        self.update()
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ManyToManyField(category)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.order_by()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_title(cls,search_category):
        image = cls.objects.filter(title__icontains=search_category)
        return image

    @classmethod
    def search_by_location(cls, location):
        image = cls.objects.filter(location=location)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__icontains=category)
        return images


