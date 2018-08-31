from django.shortcuts import render
from Service.models import Service
from django.core.paginator import Paginator
from django.http import JsonResponse
from NB_CMDB.views import getPage
# Create your views here.

def server(request, page = 1):
	allData = Service.objects.all()

	pager = Paginator(allData, 10)

	cur_page = pager.page(int(page))


	return render(request, "ServerList.html",{"pageData":cur_page,"page_range":pager.page_range})
def ServerAjax(request):
	return render(request, "ServerList_vue.html")

def AjaxServer(request, page=1):
	sql = "select * from Service_service"
	page_data = getPage(sql = sql, page = int(page))
	page_range = [1,2,3,4,5,6,7,8]
	page_data['page_range'] = page_range
	return JsonResponse(page_data)

def vue_demo(request):
	return render(request, "vueDemo.html")
