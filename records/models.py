
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=40,default="")
    def __str__(self):
        return self.book_name
    
class Address(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=100,default="")
    address_type=models.CharField(max_length=40,default="")


    
class Book_price(models.Model):
    bookname=models.ForeignKey(Book,on_delete=models.CASCADE)
    book_price=models.CharField(max_length=40,default="")

    

