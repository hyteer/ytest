from django import forms


class LabelForm(forms.Form):
	"""docstring for NameForm"forms.Formf __init__(self, arg):
		super(NameForm,forms.Form.__init__()
		self.arg = arg
	"""
	label_name = forms.CharField(label='Lanel name', max_length=50)
	#email = forms.EmailField(label='Email')
	#password = forms.PasswordInput(lanel='Password')




