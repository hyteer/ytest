from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chat'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.home, name='index'),
    #url(r'^login/$', auth_views.login),
    #url(r'^chat/$', views.chat_room, name='chat_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
    
]