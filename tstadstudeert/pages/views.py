from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import School, Study, Campus, Article
from django.core.exceptions import ObjectDoesNotExist
from pprint import pprint
import sys


def home(request):
    articles = Article.objects.all()

    return render_to_response('pages/home.html',  {'articles': articles})
    
    
def nieuws(request):
    articles = Article.objects.all()
    
    return render_to_response('pages/nieuws.html', {'articles': articles})
    

    
def praktisch(request):
    studies = Study.objects.all()
    studyID = request.GET.get('id', 0)
    schools = School.objects.all()
    campussen = Campus.objects.all()
    try:
        studyobj = Study.objects.get(pk=studyID)
        schoolobj = studyobj.study_school_name
        campusobj = studyobj.study_campus_name
    except ObjectDoesNotExist:
        studyobj = None
        schoolobj = None
        campusobj = None
    return render_to_response('pages/praktisch.html',{'studies': studies, 'studyID': studyID, 'studyobj': studyobj, 'schoolobj': schoolobj, 'campusobj': campusobj})
    
    
def testimonials(request):
    context_data = ""

    return render(request, 'pages/testimonials.html', dict(context_data))

def links(request):
    context_data = ""

    return render(request, 'pages/links.html', dict(context_data))

def chat(request):
    context_data = ""

    return render(request, 'pages/chat.html', dict(context_data))

def save_events_json(request):
    if request.is_ajax():
        if request.method == 'POST':
            print 'Raw Data: "%s"' % request.body   
    return HttpResponse("OK")