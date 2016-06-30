from __future__ import unicode_literals
from ..login_reg_app.models import User
from django.db import models

class Achieved(models.Model):
	user_id = models.ForeignKey(User)
	final_image = models.CharField(max_length=100)
	goal_name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	completion_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
