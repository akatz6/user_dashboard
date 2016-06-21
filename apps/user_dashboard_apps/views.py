from django.shortcuts import render, HttpResponse, redirect
from . models import Register



# Create your views here.
def index(request):
	print Register.objects.all();
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
		errors = Register.userManager.login(first_name, last_name, email_address,
			password, confirm_password)
		context ={
		 'errors': errors[1]
		}
	return render(request, 'user_dashboard_apps/register.html', context)

def validate_password(request):
	if request.method == 'POST':
		email_address = request.POST['email_address']
		password = request.POST['password']
		errors = Register.userManager.validate(email_address,
			password)
		if errors[1] == 9:
			context = {
			"users": Register.objects.all()
			}
			return render(request, 'user_dashboard_apps/admindashboard.html', context)
		elif errors[1] == 0:
			return render(request, 'user_dashboard_apps/dashboard.html')
		context = {
		'errors': errors[1]
		}
		return render(request, 'user_dashboard_apps/login.html', context)
	context = {
			"users": Register.objects.all()
			}
	return render(request, 'user_dashboard_apps/admindashboard.html', context)


def remove(request, id):
	Register.userManager.remove_element(id)
	context = {
			"users": Register.objects.all()
			}
	return render(request, 'user_dashboard_apps/admindashboard.html', context)

def edit(request, id):
	context ={
	"user" : Register.userManager.get(id =id)
	}
	return render(request, 'user_dashboard_apps/admin_edit.html', context)

def admin_edit(request, id):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email_address = request.POST['email_address']
	user_perm = request.POST['user_perm']
	Register.userManager.admin_edit(id, first_name, last_name, email_address, user_perm)
	context ={
	"users": Register.objects.all()
	}
	return render(request, 'user_dashboard_apps/admindashboard.html', context)

def password_edit(request, id):
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']
	password_edit(id, password, confirm_password)
	context ={
	"users": Register.objects.all()
	}
	return render(request, 'user_dashboard_apps/admindashboard.html', context)

	
