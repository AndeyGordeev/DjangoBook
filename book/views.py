from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
import datetime
# Create your views here.
from django.template import Template, Context
from django.template.loader import get_template

from book.models import Book


def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Enter a search term.')
        elif len(q) > 20:
            error.append('Please enter ar most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html',
                                      {'books': books, 'query': q})
    return render_to_response('search_form.html',
                              {'error': error})

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