from django.http import HttpResponse


def home(req):
	return HttpResponse('main page.')
	pass
