from django import forms


class NameForm(forms.Form):
	"""docstring for NameForm"forms.Formf __init__(self, arg):
		super(NameForm,forms.Form.__init__()
		self.arg = arg
	"""
	your_name = forms.CharField(label='Your name', max_length=100)
	#email = forms.EmailField(label='Email')
	#password = forms.PasswordInput(lanel='Password')

class LoginForm(forms.Form):
	"""docstring for NameForm"forms.Formf __init__(self, arg):
		super(NameForm,forms.Form.__init__()
		self.arg = arg
	"""
	username = forms.CharField(label='Username', max_length=100)
	#email = forms.EmailField(label='Email')
	password = forms.CharField(label='Password', widget=forms.PasswordInput())


class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

