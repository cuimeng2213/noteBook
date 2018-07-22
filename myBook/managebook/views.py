from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .form import BookForm
import time

# Create your views here.


def index(request):
	return render(request, 'base.html')

class bookView(ListView):

	template_name = 'base.html'
	model = Book
	context_object_name = 'book_obj'

	def get_queryset(self):
		allBook = super(bookView, self).get_queryset()

		#获取参数信息
		pageNum = self.request.GET.get('pageNum',1)
		
		self.paths = self.request.path.split('/')
		print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQ:', self.paths[-1])

		print('########### ',pageNum)
		self.type = self.request.GET.get('type','')
		self.status = self.request.GET.get('status','')
		self.search = self.request.GET.get('search','')

		for p in self.paths:
			#进入图书管理页面
			# if p == 'book':
			# 	return self.bookManage()
			#进入图书详细信息页面
			if p == 'detail':
				return self.detailView()

		#搜索实现
		if self.type and self.status:
			allBook = self.model.objects.filter(
				(Q(name__icontains=self.search) | Q(author__name__icontains=self.search)) 
				& Q(type=self.type) & Q(status = self.status)
				)
		elif self.type:
			allBook = self.model.objects.filter(
				(Q(name__icontains=self.search) | Q( author__name__icontains=self.search) )
				& Q(type=self.type)
			)
		elif self.status:
			allBook = self.model.objects.filter(
				(Q(name__icontains=self.search) | Q(author__name__icontains=self.search))
				&Q(status=self.status)
				)
		elif self.search:
			allBook = self.model.objects.filter(
					Q(name__icontains = self.search) | Q(author__name__icontains=self.search)
				)

		#分页设置
		pager = Paginator(allBook, 3)
		currentPage = pager.page(pageNum)
		return currentPage

	def get_context_data(self, **kwargs):
		context = super(bookView,self).get_context_data(**kwargs)
		#添加包含的书类型
		typeBook = TypeBook.objects.all()
		context['typeBook'] = typeBook

		#添加搜索字段信息
		if self.type:
			context['curType'] = int(self.type)
		if self.status:
			context['curStatus'] = int(self.status)

		context['curSearch'] = self.search
		print('##########context: ',context)
		return context

	# def bookManage(self):
	# 	self.template_name = 'book.html'
	# 	self.model = Book
	# 	self.context_object_name = 'book_obj'
	# 	books = self.model.objects.all()
	# 	return books

	def detailView(self):
		self.bookId = self.request.GET.get('bookId',0)
		self.template_name = 'detail.html'
		self.model = Book
		self.context_object_name = 'info_obj'
		try:
			#通过Book对象获取的info为OneToOne属性对象，在获取到的对象中会有一个info属性即对应的Detail对象实例
			info = self.model.objects.get(info__id=self.bookId)
			data = {'info_obj':info}
			#print('>>>>>>>>>>>>>>>>>>>>>>>>>>: ',dir(info))
		except ValueError as e:
			print('DDDDDDDDDDDDDDDDDDDDDDD: ',e)
			info = {}
		return info
class BookManage(ListView):
    template_name = 'book.html'
    model = Book
    context_object_name = 'book_obj'
    def get_queryset(self):
        queryset = super(BookManage, self).get_queryset()
        return  queryset

    def get_context_data(self, **kwargs):
        content = super(BookManage, self).get_context_data(**kwargs)
        bookForm = BookForm()
        content['bookForm'] = bookForm
        return  content