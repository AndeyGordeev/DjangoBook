from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
# Create your views here.

def hello(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.' % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it will be %s.</body></html>'% (offset,dt)
    return HttpResponse(html)