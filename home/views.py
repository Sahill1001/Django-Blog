from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html', context)

def search(request):
    query=request.GET.get("query")
    if len(query)>70:
        allPosts=[]
        messages.error(request, 'Query is too long')
    else:   
        allPostsTitle= Post.objects.filter(title__contains=query)
        allPostsContent= Post.objects.filter(content__contains=query)
        allPostsAutor= Post.objects.filter(author__contains=query)
        allPostsTitCont=allPostsTitle.union(allPostsContent)  
        allPosts=allPostsAutor.union(allPostsTitCont)  
    if len(allPosts) < 1 :
        messages.warning(request, 'No search result found please refine your query')
    else:
        messages.success(request, f'{len(allPosts)} Result found.')
    context={'allPosts':allPosts,'query':query}
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



def handleUser(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if User.objects.filter(username = username).first():
            messages.error(request,f"{username} username is already taken please try something different.")
            return redirect('Home')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('Home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('Home')
         
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder account has been successfully created")
        return redirect('Home')
    
    else:
        return HttpResponse("404 - Not found")
    
    
    
def handleLogin(request):
    if request.method=="POST":
        username = request.POST['loginusername']
        password = request.POST['loginpass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in successfully.")
            return redirect("Home")
        else:
            messages.error(request,"Invalid credentials. please try again.")
            return redirect("Home")
    else:
        return HttpResponse("404- Not Found")
      
def handleLogout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect("Home")
    
    
