from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


def index(request):
	return render(request, 'base.html')

class bookView(ListView):
	template_name = 'base.html'
	model = Book
	context_object_name = 'book_obj'