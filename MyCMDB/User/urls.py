from django.conf.urls import url

from .views import index, uploadFile

urlpatterns = [
	url(r'^$', index),
	url(r'uploadfile', uploadFile),
]