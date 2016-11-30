from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

def home(req):
	return render(req, 'index.html')
	#return HttpResponse('main page.')
	pass

def about(req):
	return render(req, 'about.html')
	#return HttpResponse('main page.')

def bootest(req):
	return render(req, 'bootest.html')

@login_required()
def contact_us(req):
	if req.method == 'POST':
		form = ContactForm(req.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			recipients = ['40577190@qq.com']
			if cc_myself:
				recipients.append(sender)
				send_mail(subject, message, sender, recipients)
				return HttpResponse('we have been send a mail to u, thanks.')
	else:
		form = ContactForm()
		return render(req, 'crm/mail.html', {'form': form})
