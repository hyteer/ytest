from django.shortcuts import render
from django.http import HttpResponse, Http404

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