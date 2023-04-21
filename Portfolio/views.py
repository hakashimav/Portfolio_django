from django.shortcuts import render, redirect
from django.template import loader
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.http import Http404
import os

# Create your views here.
def index(request):

    context = {
        'home':"home"
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def about(request):
    
    context = {
        'about':"About"
    }

    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

def service(request):
    
    context = {
        'service':"Service"
    }

    template = loader.get_template('service.html')
    return HttpResponse(template.render(context, request))

def realisation(request):
    
    context = {
        'realisation':"Realisation"
    }

    template = loader.get_template('realisation.html')
    return HttpResponse(template.render(context, request))