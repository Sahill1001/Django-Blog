from django.shortcuts import render,HttpResponse
from blog.models import Post,BlogComment

# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comment=BlogComment.objects.get(post=post)
    context={'post':post,'comment':comment}
    return render(request,'blog/blogPost.html',context)

def blogComment(request):
    if request.method=='POST':
        
