from django import forms
from .models import EmailSignUp

class EmailForm(forms.ModelForm):
	class Meta:
		model = EmailSignUp
		fields = ["email"]