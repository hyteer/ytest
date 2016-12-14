from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

app_name = 'demo'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^echart/$', views.echart, name='echart'),
    url(r'^piechart/$', views.piechart, name='piechart'),
    url(r'^multibar/$', views.multibarchart, name='multibar'),
    url(r'^test/$', views.test, name='test'),
    #url(r'^getname/$', views.get_name, name='get_name'),
    #url(r'^secret/$', views.secret, name='secret'),
]