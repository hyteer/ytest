from django import forms


class RoomLabelForm(forms.Form):
	"""docstring for NameForm"forms.Formf __init__(self, arg):
		super(NameForm,forms.Form.__init__()
		self.arg = arg
	"""
	room_label = forms.CharField(label='Room label', max_length=50)
	#email = forms.EmailField(label='Email')
	#password = forms.PasswordInput(lanel='Password')




