"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
from tool import views as tool_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^add/$', tool_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', tool_views.add2, name='add2'),
    url(r'^time/(\d+)/$', tool_views.time_convert, name='time_convert'),
    url(r'^polls/', include('polls.urls'), name="polls"),
    url(r'^tool/', include('tool.urls')),

]
