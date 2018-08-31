from django.db import models

# Create your models here.

class Token(models.Model):
	value = models.CharField(max_length=32, verbose_name="token值")
	time = models.IntegerField(verbose_name="token过期时间")
	create_time = models.DateTimeField(verbose_name="token创建时间")
	user_id = models.SmallIntegerField(verbose_name="用户id")
