# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render


#def home(request):
#    return render(request, 'index.html')

def nojs(request):

    r = HttpResponse(status=200)

    ua = request.META['HTTP_USER_AGENT']
    if 'Chromium' in ua:
        tpl = 'nojs/chromium.html'
    elif 'Chrome' in ua:
        tpl = 'nojs/chrome.html'
    elif 'Firefox' in ua:
        tpl = 'nojs/ff.html'
    elif 'Safari' in ua:
        tpl = 'nojs/safari.html'
    elif 'Opera' in ua:
        tpl = 'nojs/opera.html'
    elif 'MSIE' in ua:
        tpl = 'nojs/ie.html'
    else: #'Unknown'
        tpl = 'nojs/unknown.html'

    ctx = {'pagefrom': request.GET.get('page', '/'),
           'ua': ua}

    return render_to_response(tpl, ctx)