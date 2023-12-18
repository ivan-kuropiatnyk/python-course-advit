from django.conf.urls import url
from . import views#import a file views from the actual folder

urlpatterns = [
    url(r'^$', views.index, name='index'),#show from a file views.py imported function index
]
