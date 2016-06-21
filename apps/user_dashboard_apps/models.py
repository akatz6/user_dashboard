from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import bcrypt
from django.db import models
import re
from django.contrib import messages
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def login(self, first_name, last_name, email_address, password, confirm_password):

		errors = []
		errors.append(self.validate_length(first_name, 'first_name', 2, "First name is too short"))
		errors.append(self.validate_length(last_name, 'last_name', 2, "Last name is too short"))
		errors.append(self.password_match(password, confirm_password))
		errors.append(self.validate_email(email_address))

		error = []
		print errors
		for elements in range(0, len(errors)):
			try:
				errors[elements][1]
				error.append(errors[elements][1])
			except:
				pass
		error2 = {}
		for d in error:
			error2.update(d)
		if not bool(error2):
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
			success = {}
			success['success'] = "Registeration comeplete, please log in"
			return (True, success)
		else:
			return (False, error2)

	def validate_length(self, test, name, alength, error_string):
		errors = {}
		if len(test) < alength:
			print test
			errors[name] = error_string
			return(False, errors)

	def password_match(self, password, confirm_password):
		errors = {}
		if password != confirm_password:
			errors['confirm_password'] = "Passwords must match"
			return(False, errors)
		elif len(password) < 2 or len(confirm_password) < 2:			
			errors['confirm_password'] = "Password is too short"
			return(False, errors)

	def validate_email(self, email_address):
		errors = {}
		if not EMAIL_REGEX.match(email_address):
			errors['email'] = "Please enter a valid email"
			return(False, errors)

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
