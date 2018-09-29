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

   if 'category' in request.GET and request.GET["category"]:
       search_term = request.GET.get("category")
       searched_categories = Category.search_by_category(search_term)
       message = f"{search_term}"

       return render(request, 'search.html',{"message":message,"categories": searched_categories})

   else:
       message = "No related search found"
       return render(request, 'search.html',{"message":message})