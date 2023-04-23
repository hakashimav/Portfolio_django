from django.shortcuts import render, redirect
from django.template import loader
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.http import Http404

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives

from datetime import datetime

from django.core.mail import EmailMessage
# Create your views here.
def index(request):

    context = {
        'home':"Home"
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def about(request):
    
    context = {
        'about':"A propos"
    }

    template = loader.get_template('pages/about.html')
    return HttpResponse(template.render(context, request))

def service(request):
    
    context = {
        'service':"Service"
    }

    template = loader.get_template('pages/service.html')
    return HttpResponse(template.render(context, request))

def realisation(request):
    
    context = {
        'realisation':"Realisation"
    }

    template = loader.get_template('pages/realisation.html')
    return HttpResponse(template.render(context, request))


def contact(request):

    nom = request.POST['nom']
    from_email = request.POST['from_email']
    numero = request.POST['numero']
    subject = request.POST['subject']
    message = request.POST.get('message',"")

    email = EmailMessage()

    email.subject = subject
    email.body = message
    email.from_email = from_email
    email.to = 'michmav28@gmail.com'
    email.extra_headers = nom, numero
    email.reply_to = from_email

    context = {
        'send':'Message envoyé'
    }


    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))