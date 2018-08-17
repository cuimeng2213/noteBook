import os
from django.shortcuts import render
from django.http import JsonResponse
from Users.forms import CMDBUserForm
from Service.models import CMDBUser
from NB_CMDB.settings import BASE_DIR
# Create your views here.

def register(request):
	result = {'status':'success'}
	if request.method == 'POST':
		print('>>>注册用户')
		formData = CMDBUserForm(data=request.POST, files=request.FILES)
		print('>>>>>>>>>>>>>: ',formData.is_valid())
		if formData.is_valid():
			try:
				cleanData = formData.cleaned_data
				user = CMDBUser()
				user.username = cleanData.get('username')
				user.password = cleanData.get('password')
				user.nickname = cleanData.get('nickname')
				user.phone = cleanData.get('phone')
				user.email = cleanData.get('email')
				user.photo = cleanData.get('photo').name
				user.save()
				files= request.FILES.get('photo')
				savePath = os.path.join(BASE_DIR+'\\static\\images\\'+files.name)
				with open(savePath,'wb') as f:
					for chunk in files.chunks():
						f.write(chunk)
			except Exception as e:
				print('AAAAAAAA: ',e)

		return JsonResponse(result)
	else:
		result['status'] = 'error'
		return JsonResponse(result)