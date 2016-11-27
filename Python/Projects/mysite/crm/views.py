from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
	return render(req, 'crm/index.html')

def detail(req):
	return render(req, 'crm/detail.html')

def info(req, customer_id):
	customer = get_object_or_404(Question, pk=customer_id)
	records = customer.followrecords_set
	
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
