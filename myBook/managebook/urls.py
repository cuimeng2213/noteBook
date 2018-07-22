from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', bookView.as_view(), name='index'),
    url(r'^detail$', bookView.as_view(), name='detail'),
    url(r'^book$', BookManage.as_view(), name='book'),
]