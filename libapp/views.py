from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request , 'pages/index.html' , {"books":books , "categories":categories})
def books(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request , 'pages/books.html' ,{"books":books , "categories":categories})
def delete(request):
    categories = Category.objects.all()
    return render(request , 'pages/delete.html' , { "categories":categories})
def update(request):
    categories = Category.objects.all()
    return render(request , 'pages/update.html' , { "categories":categories})
