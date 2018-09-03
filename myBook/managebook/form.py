#coding: utf-8

from django import forms
from django.forms import widgets
from .models import *

'''
name = models.CharField(max_length=20, verbose_name='书名')
publish_year = models.DateField(verbose_name='出版年份')
publish_add = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
price = models.IntegerField(verbose_name='价格')
stocks = models.IntegerField(verbose_name='库存')
status = models.BooleanField(default=True, verbose_name='出版状态')
type = models.ForeignKey('TypeBook')
author = models.ManyToManyField('Author')
publisher = models.ForeignKey('Publisher')
info = models.OneToOneField('Details', blank=True, null=True, unique=True)
'''

class BookForm(forms.Form):
	'''
	图书添加表单
	'''
	name = forms.CharField(max_length=32, min_length=2, 
		widget=widgets.TextInput( attrs={'class':'form-control','placeholder':'书名','id':'bookname'} )
		)
	publisher_year = forms.DateField(
		widget = widgets.DateInput(
			attrs={'class':'form-control','placeholder':'出版日期','id':'publisher_year'}),
		)

	price = forms.IntegerField(
		widget = widgets.NumberInput(attrs={'class':'form-control','placeholder':'价格','id':'price'})
		)
	stocks = forms.IntegerField(
		widget = widgets.NumberInput(attrs={'class':'form-control','placeholder':'库存','id':'stocks'})
		)
	status = forms.ChoiceField(
		choices = [(0,'未出版'),(1,'已出版')],
		widget=widgets.Select(attrs={'class':'selectpicker',
			'type':'select','id':'status'}),
		)

	type = forms.ChoiceField(
		choices = TypeBook.objects.all().values_list('id','type_book'),
		widget = widgets.Select(attrs={'class':'selectpicker','placeholder':'类型','id':'type'})
		)
	publisher = forms.ChoiceField(
		choices = Publisher.objects.all().values_list('id','name'),
		widget = widgets.Select(
			attrs = {"class": "selectpicker", "data-live-search": "true", "data-width": "100%", "id": "publisher",}
			)
		)
	author = forms.MultipleChoiceField(
		choices = Author.objects.all().values_list('id','name'),
		widget = widgets.SelectMultiple(
			attrs = {"id": "demo-cs-multiselect"}
			)
		)
class DetailForm(forms.Form):
	chapter = forms.IntegerField(
		 widget = widgets.NumberInput(
		 		attrs = {'class':'form-control','id':'chapter','placeholder':'章节'},
		 	)
		)
	pages = forms.IntegerField(
		 widget = widgets.NumberInput(
		 		attrs = {'class':'form-control','id':'pages','placeholder':'页数'},
		 	)
		)
	words = forms.IntegerField(
		 widget = widgets.NumberInput(
		 		attrs = {'class':'form-control','id':'words','placeholder':'字数'},
		 	)
		)
	contentinfo = forms.CharField(
		 widget = widgets.Textarea(
		 	attrs = {'rows':'8','class':'form-control','id':'demo-textarea-input-1','placeholder':'内容简介'}
		 	)
		)
	catalog = forms.CharField(
		widget = widgets.Textarea( attrs={'class':'form-control','id':'demo-textarea-input-2','placeholder':'目录'})
		)
	logo = forms.ImageField(
		widget = widgets.FileInput(
			attrs={'id':'file_logo',"class": 'fileinput-new btn btn-primary btn-file'}
			)
		)
		
class AuthorForm(forms.Form):
	name = forms.CharField(
		widget = widgets.TextInput( 
				attrs = {"class":"form-control", "id":"author_name","placeholder":"作者名字"}
			)
	)
	address = forms.CharField(
		widget = widgets.TextInput( 
				attrs = {"class":"form-control", "id":"author_address","placeholder":"地址"}
			)
	)
	phone = forms.CharField(
		widget = widgets.TextInput( 
				attrs = {"class":"form-control", "id":"author_phone","placeholder":"电话"}
			)
	)
	email = forms.EmailField(
		widget = widgets.EmailInput( 
				attrs = {"class":"form-control", "id":"author_email","placeholder":"Email"}
			)
	)
	userinfo = forms.CharField(
		widget = widgets.Textarea( attrs={'class':'form-control','id':'author_userinfo','placeholder':'作者简介'})
	)
	