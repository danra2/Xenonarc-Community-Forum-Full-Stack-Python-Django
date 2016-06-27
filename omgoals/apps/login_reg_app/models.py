from __future__ import unicode_literals
from django import forms
from django.db import models
import re
from django.core.exceptions import ValidationError

PASSWORD_REGEX = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')


def validate_lengthGreaterThanTwo(value):
	if len(value)<3:
		raise ValidationError('{} must be longer than: 2'.format(value))
def validate_password(value):
	if not PASSWORD_REGEX.match(value):
		raise ValidationError('Password must be at least 8 characters')

class UserManager(models.Manager):
	def validate_confirm(request, password, confirm):
		if password == confirm:
			return True
		return False

	def login(request, email, password):
		if User.userManager.filter(email=email, password=password):
			return True
		return False

class User(models.Model):
	USER_LEVELS = (
		(1, 'Normal'),
		(9, 'Admin')
	)
	first_name = models.CharField(max_length=200, validators=[validate_lengthGreaterThanTwo])
	last_name = models.CharField(max_length=200, validators=[validate_lengthGreaterThanTwo])
	email = models.EmailField(max_length=45)
	password = models.CharField(max_length=200, validators=[validate_password])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user_level = models.SmallIntegerField(default=1, choices=USER_LEVELS)
	description = models.TextField(max_length=1000)
	userManager = UserManager()