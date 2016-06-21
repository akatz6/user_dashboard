from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import bcrypt
from django.db import models
import re
from django.contrib import messages
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def login(self, first_name, last_name, email_address, password, confirm_password):
		valid = True
		errors = {}
		if len(first_name) < 2:
			errors['first_name'] = "First Name is too short"
			valid = False

		if len(last_name) < 2:
			errors['last_name'] = "Last Name is too short"
			valid = False

		if len(password) < 2:
			errors['password'] = "Password is too short"
			valid = False

		if password != confirm_password:
			errors['confirm_password'] = "Passwords must match"
			valid = False

		if not EMAIL_REGEX.match(email_address):
			errors['email'] = "Please enter a valid email"
			valid = False

		if valid:
			user_level = 0
			records = Register.objects.all();
			try: 
				records[0]
			except:
				user_level = 9
			pw_bytes = password.encode('utf-8')
			hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
			Register.objects.create(first_name = first_name, last_name = last_name,
			password = hashed, email= email_address, salt = bcrypt.gensalt(), user_level = user_level)
			errors['success'] = "Registeration comeplete, please log in'"
		return (True, errors)

	def validate(self, email_address, password):
		errors = {}
		valid = True
		try:
			registered = Register.objects.get(email = email_address)
		except:
			errors['email'] = "Email Not found"
			valid = False

		if(valid):
			pw_bytes = password.encode('utf-8')
			salt = registered.password.encode('utf-8')
			
			if bcrypt.hashpw(pw_bytes, salt) != salt:
				errors['password'] = "Email and password do not match"
				return (False, errors)
			else: 
				return (True, registered.user_level)
		else:
			return (False, errors)

	def remove_element(self, id):
		Register.objects.filter(id=id).delete()
		return True

	def admin_edit(self, id, first_name, last_name, email_address, user_perm):
		reg = Register.objects.get(id=id)
		reg.first_name = first_name
		reg.last_name = last_name
		reg.email = email_address
		if user_perm == 'Admin':
			reg.user_level = 9
		else:
			reg.user_level = 0
		reg.save()
		return True

	def password_edit(self, id, password, confirm_password):
		reg = Register.objects.get(id=id)
		reg.password
		reg.save()



class Register(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.TextField(max_length=1000)
    salt = models.TextField(max_length=1000)
    email = models.EmailField()
    user_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

      # Connect an instance of UserManager to our User model!
    userManager = UserManager()
    # Re-adds objects as a manager
    objects = models.Manager()
    # *************************
