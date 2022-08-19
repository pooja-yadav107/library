from django.contrib import admin

# Register your models here.
from .models import Book,Address
   
admin.site.register(Book)
admin.site.register(Address)
