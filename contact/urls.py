from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app = ["contact"] 

urlpatterns = [
    path('flamenco/',views.Flamenco,name="flamenco"),
    path('contact/',views.Contact,name="contact"),
    path('almanca/',views.Almanca,name="almanca"),
    path('england/',views.England,name="england"),
    path('net/',views.net,name="net"),
    
    
]