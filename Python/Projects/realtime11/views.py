# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
'''
from .forms import RoomLabelForm
from .models import Message, Room


# Create your views here.

def index(req):
	#return HttpResponse("hi...")
	if req.method == 'POST':
		form = RoomLabelForm(req.POST)
		if form.is_valid():
			room_label = form.cleaned_data['room_label']
			return HttpResponseRedirect('/realtime/%s' % room_label)
	else:
		form = RoomLabelForm()
		return render(req, 'realtime/index.html', {"form": form})

def room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)
 
    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])
 
    return render(request, "realtime/room.html", {
        'room': room,
        'messages': messages,
    })

class RoomList(generic.ListView):
	template_name = 'realtime/roomlist.html'
	context_object_name = 'room_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Room.objects.all()[:5]

def room_new(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)
 
    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])
 
    return render(request, "realtime/room_new.html", {
        'room': room,
        'messages': messages,
    })
'''