from django.conf.urls import patterns
from vendas_multytenant.views import HomeView

urlpatterns = patterns('',
   (r'^$', HomeView.as_view()),
)
