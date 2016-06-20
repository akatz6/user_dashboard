from django.shortcuts import render, HttpResponse
from . models import Register
import re
from django.contrib import messages
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your views here.
def index(request):
	return render(request, 'user_dashboard_apps/index.html')

def login(request):
	return render(request, 'user_dashboard_apps/login.html')

def register(request):
	return render(request, 'user_dashboard_apps/register.html')

def add_to_db(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		email_address = request.POST['email_address']
		valid = True

		if len(first_name) < 2:
			messages.add_message(request, messages.ERROR, 'First Name needs to be at least one characters')
			valid = False

		if len(first_name) < 2:
			messages.add_message(request, messages.ERROR, 'Last Name needs to be at least one characters')
			valid = False

		if len(password) < 2:
			messages.add_message(request, messages.ERROR, 'Password needs to be at least one characters')
			valid = False

		if password != confirm_password:
			messages.add_message(request, messages.ERROR, 'Passwords do not match')
			valid = False

		if not EMAIL_REGEX.match(email_address):
			messages.add_message(request, messages.ERROR, 'Email is not in correct format')
			valid = False

		if valid:
			pw_bytes = password.encode('utf-8')
			hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
			Register.objects.create(first_name = first_name, last_name = last_name,
			password = hashed, email= email_address, salt = bcrypt.gensalt())
			messages.add_message(request, messages.SUCCESS, 'Registeration comeplete, please log in')

	return render(request, 'user_dashboard_apps/register.html')


