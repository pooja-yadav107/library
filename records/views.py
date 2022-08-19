
# Create your views here.
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Book


def index(request):
    context = {}
    if request.GET.get('search'):
        search = request.GET.get('search')
        user = User.objects.get(username=search)
        booktable = Book.objects.filter(author=user)
        
        context ={
            'books':booktable
        }
    
    return render(request,'index.html',context)