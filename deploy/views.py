from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
# Create your views here.

def index(response):
    title={'title':'test django web html'}
    return render_to_response('main/base.html',title)
