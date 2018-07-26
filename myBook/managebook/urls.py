from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', bookView.as_view(), name='index'),
    url(r'detail$', bookView.as_view(), name='detail'),
    url(r'addbook$', BookManage.as_view(), name='book'),
    url(r'create_details$', CreateDetailsView.as_view(), name='create_details'),
    url(r'del_book$', DelBook.as_view(),name='del_book'),
    url(r'edit_book/(\d+)/$',EditBookView.as_view(), name='edit_book'),
]