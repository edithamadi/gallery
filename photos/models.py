from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Location(models.Model):
    name = models.CharField(max_length=50)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
