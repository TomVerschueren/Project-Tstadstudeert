from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import School, User, Study, Campus

def home(request):
    context_data = ""

    return render(request, 'pages/home.html', dict(context_data))

def nieuws(request):
    context_data = ""

    return render(request, 'pages/nieuws.html', dict(context_data))

    
def praktisch(request):
    context_data = ""

    return render(request, 'pages/praktisch.html', dict(context_data))

def testimonials(request):
    context_data = ""

    return render(request, 'pages/testimonials.html', dict(context_data))

def links(request):
    context_data = ""

    return render(request, 'pages/links.html', dict(context_data))

def chat(request):
    context_data = ""

    return render(request, 'pages/chat.html', dict(context_data))
