from django.conf.urls import url
from . import views

app_name = 'crm'  # set this app's namespace
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^getname/$', views.get_name, name='get_name'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login2/(?P<username>.*)/(?P<password>.*)/$', views.login_test, name='login2'),
]