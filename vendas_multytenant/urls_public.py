#coding: utf-8
from django.conf.urls import patterns, include, url
# from vendas_multytenant.views import HomeView
# from public.views import HomeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)), ## URL da página de ADMIN

    # Este tem que ficar no final, caso contrário não vai achar os outros acima
    url(r'^$', include('public.urls', namespace='public')),
    # url(r'^$', HomeView.as_view()),
)
