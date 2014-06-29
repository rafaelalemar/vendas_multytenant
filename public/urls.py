#coding: utf-8
from django.conf.urls import patterns, include, url
from public.views import HomeView

urlpatterns = patterns('public.views',
    url(r'^$', HomeView.as_view()),
)