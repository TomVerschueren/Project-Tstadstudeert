from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import School, User, Study, Campus

def home(request):
    template = loader.get_template('pages/home.html')
    return HttpResponse(template.render(request))

def nieuws(request):
    template = loader.get_template('pages/nieuws.html')
    return HttpResponse(template.render(request))
    
def praktisch(request):
    template = loader.get_template('pages/praktisch.html')
    return HttpResponse(template.render(request))

def testimonials(request):
    template = loader.get_template('pages/testimonials.html')
    return HttpResponse(template.render(request))

def links(request):
    template = loader.get_template('pages/links.html')
    return HttpResponse(template.render(request))

def chat(request):
    template = loader.get_template('pages/chat.html')
    return HttpResponse(template.render(request))
