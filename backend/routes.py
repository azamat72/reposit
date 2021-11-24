
from django.urls import path
from . views import *

app_name = "blog"


urlpatterns = [
    path('', asosiy, name = 'home'),
    path('about/', about, name= 'about'),
    path('news/', news, name= 'yangiliklar'), 
    path('single/<slug:slug>', single, name="single"), 
    path('double/<slug:slug>', double, name="double"), 

]

