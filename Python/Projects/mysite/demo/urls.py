from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'demo'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^piechart/$', views.piechart, name='piechart'),
    url(r'^multibar/$', views.multibarchart, name='multibar'),
    url(r'^test/$', views.test, name='test'),
    #url(r'^getname/$', views.get_name, name='get_name'),
    #url(r'^secret/$', views.secret, name='secret'),
    
]