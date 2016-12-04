from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from . import views
'''
app_name = 'realtime'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^roomlist/$', views.RoomList.as_view(), name='room_list'),
    #url(r'^login/$', auth_views.login),
    #url(r'^chat/$', views.chat_room, name='chat_room'),
    url(r'^room/(?P<label>[\w-]{,50})/$', views.room, name='room'),
    
]
'''