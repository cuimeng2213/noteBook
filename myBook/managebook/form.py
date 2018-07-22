#coding: utf-8

from django import forms
from django.forms import widgets

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
	name = forms.CharField(max_length=32, min_length=2, 
			widget=widgets.TextInput( attrs={'class':'form-control','placeholder':'书名'} )
			)
	publisher_year = forms.DateField(
		widget = widgets.DateInput(
			attrs={'class':'form-control','placeholder':'出版年份'}),
	)

	price = forms.IntegerField(
		widget = widgets.NumberInput(attrs={'class':'form-control','placeholder':'价格'})
	)
	stocks = forms.IntegerField(
		widget = widgets.NumberInput(attrs={'class':'form-control','placeholder':'库存'})
	)
	status = forms.ChoiceField(
		widget=widgets.Select(attrs={'class':'magic-select',
			'type':'select','id':'status'}),
	)

	type = forms.IntegerField(
		widget = widgets.NumberInput()
		)