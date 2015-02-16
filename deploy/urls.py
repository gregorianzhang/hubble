from django.conf.urls import patterns, include, url
from deploy import views


urlpatterns = patterns('',
    url(r'^',  views.index, name='index'),
    url(r'^main/',  views.main, name='main'),

    )
