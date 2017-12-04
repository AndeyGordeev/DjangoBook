from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^time/$', views.current_datetime, name='time'),
]