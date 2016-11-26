from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from django.urls import reverse


# Create your views here.
def index(req):
	latest_question_list = Question.objects.order_by('-pub_date')[0:5]
	context = {'latest_question_list': latest_question_list}
	return render(req, 'polls/index.html', context)

	'''
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
	'''
	#return render(req, 'polls/index.html')

def detail(req, question_id):
	question = get_object_or_404(Question, pk=question_id)
	'''
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	'''
	return render(req, 'polls/detail.html', {'question': question})

	#return HttpResponse("You're looking at question %s." % question_id)

def results(req, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(req, 'polls/results.html', {'question': question})

def vote(req, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=req.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the question voting form
		return render(req, 'polls/detail.html', {
			'question': question,
			'err_message': "You don't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the back button
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	finally:
		pass
    

