from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return HttpResponse('Hello')

def acc_login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password = password)
		if user is not None:
			login(request,user)
			next = request.GET.get("next")
			print(">>>>>>>>>>>>>>>>>>>>: ", next)
			if next is not None:
				return redirect(next)
			else:
				return redirect("/index/")
	return render(request,"pages-login.html")
	
@login_required
def acc_logout(request):
	logout(request)
	return redirect("/login/")