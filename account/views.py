from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from account.models import * 

# Create your views here.
def dashboard(request):
    
    context = {
        'welcome':"Bienvenue dans Administration de Mich - Mav Portfolio",
    }

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))


def upload(request):

    img = image_projet()

    img.name = request.POST['name']
    img.image = request.FILES['image']
    img.save()

    context = {
        'succes':"l'image Envoyé avec été!"
    }

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))

