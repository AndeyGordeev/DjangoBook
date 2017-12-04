from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
# Create your views here.
from django.template import Template, Context
from django.template.loader import get_template


def hello(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'mytemplate.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'futuretime.html', locals())