from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/admin/login/')
def index(response):
#    title={'title':'test django web html'}
#    print User.get_username()
    menus=["Home","server","docker","command","about"]
    title={'menus':menus,'title':"index"}

    return render_to_response('main/base.html',title)

@login_required
def main(response):
    title={'title':'test django web html'}
    return render_to_response('main/base.html',title)
