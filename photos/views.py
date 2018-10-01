from django.shortcuts import render,redirect
from .models import Image
from django.http  import HttpResponse,Http404
import datetime as dt
# Create your views here.
def welcome(request):
    return render(request, 'all-photos/today-photos.html')

def photos(request):
    photos = Image.objects.all()
    
    return render(request, 'all-photos/today-photos.html', {"photos":photos})

def search_results(request):

   if 'image' in request.GET and request.GET["image"]:
       search_term = request.GET.get("image")
       searched_images = Image.search_by_name(search_term)
       message = f"{search_term}"

       return render(request, 'all-photos/search.html',{"message":message,"image": searched_images})

   else:
       message = "No related search found"
       return render(request, 'all-photos/search.html',{"message":message})


# def water(request):
#     image Category.objects.get(name=category_name)
#     image = image.id
#     photos = Image.filter(category_id=name)

#     return render(request,'all-photos/search.html',{'photos',photos})