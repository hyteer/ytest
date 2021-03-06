from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DeleteView):
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(generic.DeleteView):
	model = Question
	template_name = 'polls/results.html'


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
		
    

