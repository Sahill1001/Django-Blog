from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact
from blog.models import Post


def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html', context)

def search(request):
    query=request.GET.get("query")
    post= Post.objects.filter(title__contains=query)
    context={'post':post}
    return render(request, 'home/search.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        dec = request.POST.get('dec', '')
        if len(name) < 3 or len(email) < 10 or len(phone) < 10 or len(dec) < 10:
            messages.error(request, 'Please enter a valid information')
        else:
            contact = Contact(name=name, email=email, phone=phone, dec=dec)
            contact.save()
            messages.success(request, 'Your complaint sent successfully')
    return render(request, 'home/contact.html')
