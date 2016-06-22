from __future__ import unicode_literals
from ..user_dashboard_apps.models import Register
from django.db import models


class UserManager(models.Manager):
	def add_message(self, id, message):
		test= Register.objects.get(id =id)
		print test
		Message.objects.create(personal_id = test, message = message)
		return True

# Create your models here.
class Message(models.Model):
	personal_id = models.ForeignKey(Register)
	message = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()

class Comment(models.Model):
	personal_id = models.IntegerField()
	message_id = models.ForeignKey(Message)
	comment = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# userManager = UserManager()
	# objects = models.Manager()