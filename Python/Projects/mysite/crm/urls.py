from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'crm'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', auth_views.login),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^getname/$', views.get_name, name='get_name'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^login2/(?P<username>.*)/(?P<password>.*)/$', views.login_test, name='login2'),
    url(r'^secret/$', views.secret, name='secret'),
    url(r'^mail/$', views.contact_us, name='contact_us'),
]