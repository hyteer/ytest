from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template import Template, Context

def debug(req):
    #import pdb; pdb.set_trace()
    return HttpResponse("Debug Info:...")

def home(req):
    return HttpResponse("congratulations! this is the django homepage.")

def time(req):
    now = datetime.datetime.now()
    html = "Server time:%s" %now
    return HttpResponse(html)


#################
def bootstrap_demo(req):
    return render(req,'bootstrap-demo.html')

def hours_ahead(req,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "Now is: %s .<br>In %s hour(s), it will be: %s ." %(datetime.datetime.now(),offset,dt)
    return HttpResponse(html)
"""
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form':
form})
"""

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form':form})

