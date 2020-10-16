from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models 
from . import forms
# Create your views here.

def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html') 

def blog(request):
    return render(request, 'blog.html')

def activity(request):
    return render(request, 'activities.html')

def blog_members(request):
    users = User.objects.all()
    dict = {'users':users}
    return render(request, 'members.html', context=dict)

def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def user_login(request):
    if request.method == "POST": 
        userN = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request,username=userN,password=password)

        if user is not None:
            login(request,user)
            return redirect('/blog/')
        else:
            return redirect('/signup_page/')

def signup(request):
    try:
        if request.method == "POST":
            userN = request.POST['user']
            email = request.POST['email']
            passw = request.POST['pass']

            user = User.objects.create_user(userN,email,passw)
            user.save()

            return redirect('/blog/members')

    except:
        return redirect('/login_page/')


def user_logout(request):
    logout(request)
    return redirect('/')


def blog_post(request):
    posts = reversed(models.Post.objects.all())
    dict = {"posts":posts}

    return render(request, 'blog_posts.html', context=dict)

def post(request, pk):
    post = models.Post.objects.get(pk=pk)
    if request.method == "POST":
        usr_comment = request.POST.get("comment")
        name = request.user.username
        comment = models.Comment(name=name, comment=usr_comment, post=post)
        comment.save()
    dict = {'post':post}

    return render(request, 'post.html', context=dict)

def add_comment(request,pk):
    post = models.Post.objects.get(pk=pk)
    name = requestuser.username
    comment = request.POST['comment']
    return redirect("/blog_post/")


def addpost(request):

    if request.method == "POST":
        form = models.Post(name=request.user.username , title=request.POST["title"], post = request.POST["post"],user_id=request.user)
        form.save()
        return redirect("/blog_post/")

    return render(request, 'addpost.html')

def del_post(request, pk):

    post = models.Post.objects.get(pk=pk)
    post.delete()

    return redirect('/blog_post/')
