from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(bookView.as_view()), name='index'),
    url(r'detail$', login_required(bookView.as_view()), name='detail'),
    url(r'addbook$', login_required(BookManage.as_view()), name='book'),
    url(r'create_details$', login_required(CreateDetailsView.as_view()), name='create_details'),
    url(r'del_book$', login_required(DelBook.as_view()),name='del_book'),
    url(r'edit_book/(\d+)/$',login_required(EditBookView.as_view()), name='edit_book'),	
	url(r'author/$',login_required(AuthorView.as_view()), name="author_manage"),
	url(r'publisher/$',login_required(PublisherView.as_view()), name="publisher_manage"),
]