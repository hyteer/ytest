from django.http import HttpResponse
from django.shortcuts import render


def home(req):
	return render(req, 'index.html')
	#return HttpResponse('main page.')
	pass
