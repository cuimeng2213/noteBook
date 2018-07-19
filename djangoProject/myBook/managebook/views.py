from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *

# Create your views here.


def index(request):
	return render(request, 'base.html')

class bookView(ListView):
	template_name = 'base.html'
	model = Book
	context_object_name = 'book_obj'

	def get_queryset(self):
		
		pageNum = self.request.GET.get('pageNum',1)
		print('########### ',pageNum)
		self.type = self.request.GET.get('type','')
		self.status = self.request.GET.get('status','')
		self.search = self.request.GET.get('search','')

		queryset = super(bookView, self).get_queryset()

		#搜索实现
		if self.search and self.status:
			allBook = self.model.objects.filter(
				Q(name__icontains=search) | Q()

				)
		elif self.search:
			allBook = self.model.objects.filter(
					name__icontains = self.search
				)
		else:
			allBook = self.model.objects.all()

		#分页设置
		pager = Paginator(allBook, 3)
		currentPage = pager.page(pageNum)
		print(currentPage)

		return currentPage

	def get_context_data(self, **kwargs):
		context = super(bookView,self).get_context_data(**kwargs)
		typeBook = TypeBook.objects.all()
		context['typeBook'] = typeBook
		print('##########context: ',context)
		return context