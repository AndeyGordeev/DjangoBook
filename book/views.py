from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
import datetime
# Create your views here.
from django.template import Template, Context
from django.template.loader import get_template

from DjangoBook import settings
from book.models import Book


def contact_thanks(request):
    return HttpResponse('Thanks for visiting!')

def contact(request):
    error=[]
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            error.append('Enter a subject.')
        if not request.POST.get('message', ''):
            error.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            error.append('Enter a valid e-mail address.')
        if not error:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', settings.EMAIL_HOST_USER),
                [request.POST['email']], fail_silently=False,
            )
            return contact_thanks(request)
    return render(request, 'contact_form.html', {
        'error': error,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })

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