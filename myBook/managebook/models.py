from django.db import models

class TypeBook(models.Model):
	type_book = models.CharField(max_length=32, verbose_name='')
	def __str__(self):
		return self.type_book

class Author(models.Model):
	name = models.CharField(max_length=32, verbose_name='作者名字')
	address = models.CharField(max_length=32, verbose_name='地址')
	phone = models.CharField(max_length=11, verbose_name='电话')
	email = models.EmailField(verbose_name='作者邮箱')
	authorinfo = models.TextField(verbose_name='作者简介')
	def __str__(self):
		return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社名字')
    address = models.CharField(max_length=32, verbose_name='出版社地址')

    def __str__(self):
    	return self.name

class Details(models.Model):
	chapter = models.CharField(max_length=32, verbose_name='章节')
	pages= models.IntegerField(verbose_name='页数')
	words= models.IntegerField(verbose_name='字数')
	contentinfo= models.TextField(verbose_name='内容简介')
	logo = models.ImageField(verbose_name='图标')
	catalog= models.TextField(verbose_name='目录')
	

class Book(models.Model):
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

	def __str__(self):
		return self.name