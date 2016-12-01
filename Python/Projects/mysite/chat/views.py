from django.shortcuts import render
from .models import Room, Message
from .forms import LabelForm

# Create your views here.
def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)
 
    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])
 
    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })

def home(req):

	if req.method == 'POST':
		form = LabelForm(req.POST)
		if form.is_valid():
			label = form.cleaned_data['label_name']
			return HttpResponseRedirect('/chat/%s' % label)
	else:
		form = LabelForm()
		return render(req, 'chat/index.html', {'form': form})