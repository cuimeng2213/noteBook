from django.shortcuts import render
from Users.forms import CMDBUserForm
def index(request):
	forms = CMDBUserForm()
	return render(request, 'index.html', locals())

def cmdbLogin(request):
	return render(request, 'login.html')