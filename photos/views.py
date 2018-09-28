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