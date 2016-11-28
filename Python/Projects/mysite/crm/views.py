from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import NameForm, LoginForm

# Create your views here.

def index(req):
	return render(req, 'crm/index.html')

def detail(req):
	return render(req, 'crm/detail.html')

def info(req, customer_id):
	customer = get_object_or_404(Question, pk=customer_id)
	records = customer.followrecords_set
	
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def login_test(req, username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		return HttpResponse('Authenticate sucessfully.')
	else:
		return HttpResponse('Auth Fail.')

def login(req):
	if req.method == 'POST':
		form = LoginForm(req.POST)
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(username=username, password=password)
		print('username:%s' % username)
		if form.is_valid() and user is not None:
			return HttpResponseRedirect('/crm/thanks')
	else:
		form = LoginForm()
		return render(req, 'crm/login.html', {'form': form})

def get_name(req):

	if req.method == 'POST':
		form = NameForm(req.POST)
		if form.is_valid():
			return HttpResponseRedirect('/crm/thanks')
	else:
		form = NameForm()
		return render(req, 'crm/name.html', {'form': form})

def thanks(req):
	return render(req, 'crm/thanks.html')
