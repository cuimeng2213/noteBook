from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', bookView.as_view(), name='index'),
]