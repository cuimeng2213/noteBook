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
		queryset = super(bookView, self).get_queryset()

		allBook = self.model.objects.all()

		pager = Paginator(allBook, 1)

		currentPage = pager.page(pageNum)
		print(currentPage)
		return currentPage

	def get_context_data(self, **kwargs):
		context = super(bookView,self).get_context_data(**kwargs)
		typeBook = TypeBook.objects.all()
		context['typeBook'] = typeBook
		print('##########context: ',context)
		return context