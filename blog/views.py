from django.shortcuts import render

from blog.models import Post


# Create your views here.


def blog_view(request):
    return render(request,'blog/blog-home.html')


def blog_single(request):
    return render(request,'blog/blog-single.html')


def test(request):
    Posts=Post.objects.all()
    context= {'posts': Posts }
    return render(request,'test.html',context)
