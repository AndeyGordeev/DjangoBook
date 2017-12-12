from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^time/$', views.current_datetime, name='time'),
    url(r'^time/plus/([0-9]{1,2})/$', views.hours_ahead, name='plustime'),
    url(r'^another-time-page/$', views.current_datetime, name='anothertime'),
    url(r'^search/$', views.search),
]