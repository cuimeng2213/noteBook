from django.contrib import admin

from .models import *

# Register your models here.
# user : cuimeng
# password: cm123456

admin.site.register(Author)
admin.site.register(TypeBook)
admin.site.register(Publisher)
admin.site.register(Details)
admin.site.register(Book)
