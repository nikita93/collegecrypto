from django.db import models

# Create your models here.
class EmailSignUp(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now =False)
	def __unicode__(self): 
		return self.email