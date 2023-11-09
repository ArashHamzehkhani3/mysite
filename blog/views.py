from django.shortcuts import render,get_object_or_404

from blog.models import Post


# Create your views here.


def blog_view(request):
    Posts=Post.objects.all()
    context= {'posts': Posts }
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post=get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)


def test(request,pid):
    
    #post=Post.objects.get(id=pid)
    post=get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)
