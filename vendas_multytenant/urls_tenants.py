#coding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('customers.views',
    url(r'^admin/', include(admin.site.urls)), ## URL da página de ADMIN

    url(r'^login/', 'auth_login', name='login'),
    url(r'^logout/', 'auth_logout', name='logout'),
    url(r'^$', 'main', name='main'),
   # (r'^$', TenantView.as_view()),
)