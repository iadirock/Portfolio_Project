from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def allblogs(request):
    #to get objects from db and turn them into python objects
    blogs = Blog.objects
    ordered_blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'blogs/allblogs.html', {'blogs':ordered_blogs})

#creating a function to show detailed version of blog
def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogs/detail.html', {'detail_blog':detail_blog})
