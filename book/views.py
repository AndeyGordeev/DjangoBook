from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
import datetime
# Create your views here.
from django.template import Template, Context
from django.template.loader import get_template

from book.models import Book


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_form.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search form')

def search_form(request):
    return render_to_response('search_form.html')

def hello(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    values = request.META.items()
    now = datetime.datetime.now()
    return render(request, 'mytemplate.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'futuretime.html', locals())