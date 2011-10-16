from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^nojs$', 'nojs.views.nojs', name='nojs'),
)
