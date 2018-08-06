from django.db import models

# Create your models here.

class CMDBUser(models.Model):
	'''
	用户表
	'''
	username = models.CharField(max_length=32, verbose_name='用户名')
	password = models.CharField(max_length=32, verbose_name='密码')
	email = models.EmailField(verbose_name='邮箱')
	phone = models.CharField(max_length=11, verbose_name='电话号码')
	photo = models.ImageField(upload_to='images', verbose_name='头像')

	def __str__(self):
		return self.username

	class Meta:
		verbose_name ='用户表'
		verbose_name_plural = verbose_name

class Permission(models.Model):
	'''
	权限表
	'''
	name = models.CharField(max_length=32, verbose_name='权限名称')
	obj_id = models.IntegerField(verbose_name='操作对象')
	description = models.TextField(verbose_name='权限描述信息')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='权限表'
		verbose_name_plural = verbose_name

class Group(models.Model):
	name = models.CharField(max_length=32, verbose_name='用户组名')

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = '用户组'
		verbose_name_plural = verbose_name

class User_Group(models.Model):
	'''
	用户和组的关系表
	'''
	user = models.ForeignKey('CMDBUser')
	group = models.ForeignKey('Group')

class User_Permission(models.Model):
	'''
	用户和权限关系表
	'''
	user = models.ForeignKey('CMDBUser')
	permission = models.ForeignKey('Permission')

class Group_Permission(models.Model):
	'''
	组合权限关系表
	'''
	group = models.ForeignKey('Group')
	permission = models.ForeignKey('Permission')

