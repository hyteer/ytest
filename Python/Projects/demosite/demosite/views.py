from django.http import HttpResponse
from django.shortcuts import render

def home(req):
	return render(req, 'index.html')

def about(req):
	return render(req, 'about.html')

def yt(req):
	return HttpResponse("hi i'm YT...")

def debug(req):
	return HttpResponse("this is the debug page.")




