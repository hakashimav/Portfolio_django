from django.contrib import admin
from django.urls import path,include
#from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('upload', views.upload, name ='upload')
]