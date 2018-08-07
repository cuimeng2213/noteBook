from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def cmdbLogin(request):
	return render(request, 'login.html')