from django.shortcuts import render, HttpResponse
# from . models import

# Create your views here.
def index(request):
	return render(request, 'user_dashboard_apps/index.html')


def login(request):
	return render(request, 'user_dashboard_apps/login.html')

def register(request):
	return render(request, 'user_dashboard_apps/register.html')