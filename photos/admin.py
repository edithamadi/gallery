from django.contrib import admin
from .models import Location,Image,category
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Location)
admin.site.register(Image)
admin.site.register(category)