from django.conf.urls import url
from Api.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
	url(r'^$', csrf_exempt(CMDBApi.as_view()))
]