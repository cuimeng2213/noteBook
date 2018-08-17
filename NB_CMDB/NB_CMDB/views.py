from django.shortcuts import render
from Users.forms import CMDBUserForm
from django.http import JsonResponse, HttpResponseRedirect
from Service.models import CMDBUser

def login_valid(func):
	def inner(req,*args, **kwargs):
		username = req.COOKIES.get('username')
		print('#######: username', req.COOKIES)
		if username:
			return func(req)
		else:
			return HttpResponseRedirect('/login/')

	return inner

@login_valid
def index(request):
	if request.method =='POST':
		return JsonResponse({'status':'success'})
	else:
		forms = CMDBUserForm()
		return render(request, 'index.html', locals())

def cmdbLogin(request):
	if request.method == 'POST' and request.POST:
		response = render(request, 'login.html')
		#response.set_cookie('login_cookie','helloword', max_age=3600)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = CMDBUser.objects.filter(username=username)[0]
		print('CCCC: ', user.username, user.password , password)
		print('xiangdengbu',(user.password == password))
		if user.password == password:
			print('password equal ', user.password)
			response = HttpResponseRedirect('/index/') 
			response.set_cookie(key='username',value=username ,max_age=3600)
			return response
		else:
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')

@login_valid
def cmdbLogout(request):
	response = HttpResponseRedirect('/login/')
	response.set_cookie(key='username',value='') 
	return response

def echartsDemo(request):
	return render(request,'echartsDemo.html')