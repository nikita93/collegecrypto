from django.contrib import admin

# Register your models here.
from .models import EmailSignUp #to reference the signup in models
from .forms import EmailForm

class SignUpAdmin(admin.ModelAdmin): #customise what we see in the admin pannel
	list_display = ["__unicode__", "timestamp", "email"]
	form = EmailForm
	class Meta:
		model = EmailSignUp

admin.site.register(EmailSignUp, SignUpAdmin)