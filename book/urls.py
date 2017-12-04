from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
]