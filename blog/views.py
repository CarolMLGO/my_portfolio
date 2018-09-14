from django.shortcuts import render,get_object_or_404
from .models import Blog

def allblogs(request):
    blogs=Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail_blog(request,blog_id):
    d_blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail_blog.html',{'blog':d_blog})
