from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url(r'^$',views.photos,name = 'photos'),
    url(r'^search/', views.search_results, name='search_results')
]