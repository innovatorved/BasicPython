from django.shortcuts import render
from django.http import HttpResponse
from .models import Allcourses
from django.template import loader
# Create your views here.

def Course(request):
    ac=Allcourses.objects.all()
    template = loader.get_template('Nextin/Course.html')
    context={

        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request,id):
    return HttpResponse('<h1>These are the course details</h1>')

