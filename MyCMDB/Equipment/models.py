from django.db import models

# Create your models here.

class Equipment(models.Model):
	hostname = models.CharField(max_length=32, verbose_name='主机名')
	mac = models.CharField(max_length=32, verbose_name='mac地址')
	ip = models.CharField(max_length=32, verbose_name='Ip地址')
	sys_type = models.CharField(max_length=32, verbose_name='系统类型')
	cpu_count = models.IntegerField(verbose_name='CPU个数')
	disk = models.CharField(max_length=32, verbose_name='硬盘')
	memory = models.CharField(max_length=32, verbose_name='内存')

	class Meta:
		verbose_name = '设备表'
		verbose_name_plural = verbose_name