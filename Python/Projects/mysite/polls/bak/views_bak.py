from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.
def index(req):
	latest_question_list = Question.objects.order_by('-pub_date')[0:5]
	template = loader.get_template('polls/index.html')
	context = {'latest_question_list': latest_question_list}
	return HttpResponse(template.render(context,req))

	'''
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
	'''
	#return render(req, 'polls/index.html')

def detail(req, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(req, question_id):
	resp = "You're looking at the results of question %s."
	return HttpResponse(resp % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

