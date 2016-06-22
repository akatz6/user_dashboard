from django.shortcuts import render, HttpResponse, redirect
from ..user_dashboard_apps.models import Register
from .models import Message

# Create your views here.
def index(request, id):
	context = {
	'user' : Register.objects.get(id = id),
	'messages' : Message.objects.filter(personal_id = id)
	}
	return render(request, 'message_wall/index.html', context)

def message(request, id):
	message = request.POST['message']
	Message.userManager.add_message(id, message)
	messages = Message.userManager.all()
	print [m.message for m in messages]
	return redirect('/wall/' +id)
