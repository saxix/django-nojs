from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.shortcuts import render

admin.autodiscover()

def home(request):
    return render(request, 'index.html')

urlpatterns = patterns('',
    url(r'^$', home, name='home'),

    url(r'^nojs/', include('nojs.urls')),

    url(r'.*', home),
)
