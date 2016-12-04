from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def info(req):
	return render(req, 'people/info.html')

def user_logout(request):
    logout(request)
    return HttpResponse('Thanks...')