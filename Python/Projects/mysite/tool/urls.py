from django.conf.urls import url
from . import views

app_name = 'tool'	# register app's namespace
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/(\d+)/(\d+)/$', views.add2, name='add2'),
	url(r'^time/(\d+)/$', views.time_convert, name='time_convert')
	
]
