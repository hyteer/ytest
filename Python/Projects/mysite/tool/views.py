from django.shortcuts import render
from django.http import HttpResponse, Http404
import time

# Create your views here.

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(c)

def add2(request,a,b):
	a = int(a)
	b = int(b)
	c = a + b
	return HttpResponse(c)

def time_convert(req,timestamp):
	#timestamp = str(timestamp)
	timearray = time.localtime(timestamp)
	localtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	return HttpResponse(localtime)
