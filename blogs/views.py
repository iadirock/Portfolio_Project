from django.shortcuts import render
from .models import Blog

# Create your views here.

def allblogs(request):
    #to get objects from db and turn them into python objects
    blogs = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blogs':blogs})