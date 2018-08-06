from django.shortcuts import render
from django.http import HttpResponse

from PIL import Image

# Create your views here.

def index(request):
	return render(request, 'blank.html')
	
def uploadFile(request):
	if request.method == 'GET':
		return render(request, 'file.html')
	else:
		print(request.FILES['ff'])
		imgUrl = 'media/'+str(request.FILES['ff'])
		im = Image.open(request.FILES['ff'])
		im.save(imgUrl)
		return HttpResponse('<h1>HHHHHHHHHHHHHHH</h1>')