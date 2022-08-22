from django.contrib import admin

# Register your models here.
from .models import Book,Address,Book_price
   
@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ['id','author','book_name']
    


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ['id','author','address','address_type']


@admin.register(Book_price)
class Book_price(admin.ModelAdmin):
    list_display = ['id','book_price','bookname']