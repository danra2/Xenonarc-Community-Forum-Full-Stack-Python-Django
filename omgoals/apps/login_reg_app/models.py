from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
ALIAS_REGEX = re.compile(r'^[a-zA-Z0-9 _-]{2,}$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]{8,}')
class UserManager(models.Manager):

	#Login and Registration Methods

	def get_id(request, email, password):
		db_password = User.userManager.get(email=email)
		return User.userManager.get(email=email, password= bcrypt.hashpw(password.encode('UTF-8'),db_password.password.encode('UTF-8'))).id

	def login_val(request, email, password):
		db_password = User.userManager.get(email=email)
		if User.userManager.filter(email=email, password= bcrypt.hashpw(password.encode('UTF-8'),db_password.password.encode('UTF-8'))):
			return True
		return False

	def name_val(request, name):
		if NAME_REGEX.match(name):
			return True
		return False

	def email_val(request, email):
		if EMAIL_REGEX.match(email):
			if not User.userManager.filter(email=email):
				return True 
		return False
		
	def password_val(request, password):
		if PASSWORD_REGEX.match(password):
			return True
		return False

	def confirm_val(request, password,confirm):
		if password == confirm:
			return True
		return False

	def alias_val(request, alias):
		if ALIAS_REGEX.match(alias):
			return True
		return False

	def register_user(request, first, last, email, password, alias):
		User.userManager.create(first_name=first,last_name=last, email=email, password=bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt()), alias=alias)

	#Profile Methods

class User(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=45)
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	description = models.TextField(max_length=1000)
	userManager = UserManager()
	alias = models.CharField(max_length=100)

