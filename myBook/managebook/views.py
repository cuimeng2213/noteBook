from django.shortcuts import render
from django.views.generic import View, ListView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from .form import BookForm, DetailForm
import time
from myBook import settings
from PIL import Image

# Create your views here.


def index(request):
	return render(request, 'base.html')
class DelBook(View):
	def post(self, request):
		ret = {'status':'success','data':'删除成功'}
		bookId = request.POST.get('book_id')
		print('#############: ', bookId)
		book = Book.objects.get(id=int(bookId))
		book.delete()

		return JsonResponse(ret)

class CreateDetailsView(View):
	def post(self, request):
		ret = {'status':'','data':''}
		print('##############: recv: ', request.POST)
		detailForm = DetailForm(request.POST, request.FILES)
		if detailForm.is_valid():
			details_data = detailForm.cleaned_data
			details = Details()
			details.chapter = details_data['chapter']
			details.pages = details_data['pages']
			details.words = details_data['words']
			details.contentinfo = details_data['contentinfo']
			details.catalog = details_data['catalog']

			#保存图片
			logo = details_data['logo']
			location = settings.MEDIA_ROOT+'\\images\\logo\\'+str(details_data['pages'])+ \
				'_'+str(details_data['words'])+'_'+str(logo.name)
			# print('###############: location: ', location, dir(request.FILES['logo']))
			with open(location,'wb') as f:
				for d in request.FILES['logo'].chunks():
					f.write(d)

			#保存图片路径
			details.logo = location
			details.save()

			#关联对应的图书
			print('###########bookid: ', request.POST.get('book_id'))
			b = Book.objects.get(id=int(request.POST.get('book_id')))
			b.info = details
			b.save()
			ret['status'] = 'success'
			ret['data'] = '添加图书成功'
		else:
			print('############: form is_valid', detailForm.errors)
			ret['status'] = 'failed'
			ret['data'] = detailForm.errors

		return JsonResponse(ret)

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
        pageNum = self.request.GET.get('pageNum',1)
        print('##########: pageNum: ', pageNum)
        pager = Paginator(queryset, 10)
        cur = pager.page(pageNum)
        return  cur

    def get_context_data(self, **kwargs):
        content = super(BookManage, self).get_context_data(**kwargs)
        bookForm = BookForm()
        content['bookForm'] = bookForm

        details_form = DetailForm()
        content['details_form'] = details_form
        return  content
    def post(self, request):
    	ret = {'status':'success','data':''}
    	formData = BookForm(request.POST)
    	print('####:', request.POST)
    	try:
    		if formData.is_valid():
	    		cleanData = formData.cleaned_data
	    		print('####: status type=', type(cleanData['status']))
	    		book = Book()
	    		book.name = cleanData['name']
	    		book.publish_year = cleanData['publisher_year']
	    		book.price = cleanData['price']
	    		book.stocks = cleanData['stocks']
	    		book.type_id = cleanData['type']
	    		book.publisher_id = cleanData['publisher']
	    		book.status = cleanData['status']
	    		

	    		book.save()
	    		book.author.add(*cleanData['author'])
	    		print('22222222222')

	    		ret['status'] = 'success'
	    		ret['data'] = '书籍添加成功'
	    	else:
	    		print('################# vvv: ',formData.errors)
	    		ret = {'status':'failed','data':'书籍添加失败'}
    	except Exception as e:
    		print('###############: error: ', e)

    	return JsonResponse(ret)