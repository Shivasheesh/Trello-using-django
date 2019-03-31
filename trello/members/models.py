from django.db import models
from django.conf import settings

# Create your models here.

class Member(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.title

