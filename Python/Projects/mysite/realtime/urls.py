from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'realtime'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', auth_views.login),
    #url(r'^thanks/$', views.thanks, name='thanks'),
    #url(r'^getname/$', views.get_name, name='get_name'),
    #url(r'^secret/$', views.secret, name='secret'),
    
]