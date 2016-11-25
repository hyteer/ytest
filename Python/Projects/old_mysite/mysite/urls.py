"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from books import views as bookviews
from . import views
from . import settings
from tool import views as tool_views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', views.time),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^search/$', bookviews.search),
    url(r'^boot/$', views.bootstrap_demo),
    url(r'^contact/$', views.contact),
    url(r'^add/$', tool_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/', tool_views.add2, name='add2'),

]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug), ]
