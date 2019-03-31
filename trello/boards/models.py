from django.urls import reverse
from django.db import models
from django.utils import timezone
from members.models import Member
from django.contrib.auth.models import User

# Create your models here.

class Newboard(models.Model):
	board = models.ForeignKey('Board', on_delete=models.PROTECT, null=True, blank=True)
	member =models.ForeignKey(Member, on_delete=models.PROTECT)
	notes = models.TextField(null=True, blank=True)
	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return str(self.board.id)
		except:
			return self.member.title


VAR_MEMBERS=(
	('User1', 'User1'),
	('User2', 'User2'),
	('User3', 'User3'),
	('User4', 'User4'),
	('User5', 'User5'),	
	)

class Board(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	members = models.CharField(max_length=120, choices=VAR_MEMBERS, default='user1')

	def __unicode__(self):
		return self.title

