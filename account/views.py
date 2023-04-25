from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    context = {
        'welcome':"Bienvenue dans Administration de Mich - Mav Portfolio",
    }

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))