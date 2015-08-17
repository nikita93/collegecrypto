from django.shortcuts import render
from django.conf import settings
# Create your views here.
from .forms import EmailForm

def home(request):
	title = " "
	form = EmailForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form
	}
	if form.is_valid():
		form.save()
		context = {
			"title": "thank you"
		}
	return render(request, "home.html", context)
def email_collect(request):
	title = "Sign up for our newletter!"
	form = EmailForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form
	}
	if form.is_valid():
		form.save()
		context = {
			"title": "thank you"
		}
	return render(request, "email_collect.html", context)	
def about(request):
	return render(request, "about.html")
def contact(request):
	return render(request, "contact.html", {})