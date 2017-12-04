from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.' % now
    return HttpResponse(html)