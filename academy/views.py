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
    dict = {}

    return render(request, 'activities.html', context=dict)

def blog_members(request):
    users = User.objects.all()
    users_count = users.count() - 1
    dict = {'users':users,'users_count':users_count}
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

def event(request):
    form = forms.EventForm
    if request.method == "POST":
        form = forms.EventForm(request.POST)
        if form.is_valid:
            form.save(commit=True)

    dict = {'form':form, 'event':models.Event.objects.all}

    return render(request, 'event.html', context=dict)

def seeevent(request,pk):
    event = models.Event.objects.get(pk=pk)

    if request.method == "POST":
        rule = request.POST['rule']

        event_rule = models.EventRule(event=event, rule=rule)
        event_rule.save()

    dict = {'event':event}

    return render(request, 'seeevent.html', context=dict)

def del_event(request,pk):

    event = models.Event.objects.get(pk=pk)
    event.delete()

    return redirect('/blog/events/')


def quizes(request):
    quiz = models.Quiz.objects.all()

    dict = {'quizes':quiz}

    return render(request, 'quizes.html', context=dict)

def part(request, state, pk):
    given = False
    quiz = models.Quiz.objects.get(pk=pk)
    for r in models.Result.objects.filter(quiz=quiz):
        if r.user == request.user.username:
            given = True
    ques = models.QuizQue.objects.filter(quiz=quiz)
    time = quiz.date_time
    dict = {'quiz':quiz,'state':state,'ques':ques,'given':given,'time':time}

    if request.method == 'POST':
        if quiz.quiz_status == 'open':
            result = 0
            for q in ques:
                if request.POST[q.ques] =="R":
                    result += 1
            final_result = models.Result(quiz=quiz, user=request.user.username, result=str(result))
            final_result.save()
            return redirect(f'/quizes/')
        else:
            return redirect('/quizes/')
    return render(request, 'part.html', context=dict)

def result(request):
    quiz = reversed(models.Quiz.objects.all())
    result_obj = models.Result.objects.all()
    dict = {'result':result_obj,'quizes':quiz}

    return render(request, 'result.html', context=dict)

def result_event(request,pk):
    quiz = models.Quiz.objects.get(pk=pk)
    result = models.Result.objects.filter(quiz=quiz)
    marks_list = []
    for r in result:
        marks_list.append(r.result)
    marks_list.sort()
    highest = marks_list[len(marks_list)-1]
    lowest = marks_list[0]
    dict = {'result':result,'quiz':quiz,'highest':highest}

    return render(request, 'result_event.html', context=dict)

def addquestion(request,pk):
    quiz = models.Quiz.objects.get(pk=pk)
    ques = models.QuizQue.objects.filter(quiz=quiz)
    ans = models.QuizAns.objects.filter(quiz=quiz)
    result = models.Result.objects.filter(quiz=quiz)

    time = quiz.time
    if time > 60:
        minutes = time % 60
        hour = time // 60
        if hour == 1:
            hour_count = 'hour'
        else:
            hour_count = 'hours'
        if minutes == 0 or  minutes == 1:
            minutes_count = 'minute'
        else:
            minutes_count = 'minutes'
        time = f'{hour} {hour_count} and {minutes} {minutes_count} '
    elif time<=60:
        time = f"{time} minutes"

    dict = {'quiz':quiz,'ques':ques,'ans':ans,'pk':pk,'result':result,'time':time}

    return render(request, 'addquestion.html', context=dict)

def addquestion_fun(request):
    pk = request.POST['pk']
    quiz = models.Quiz.objects.get(pk=pk)
    ques = request.POST['question']
    ans = request.POST['answer']

    question = models.QuizQue(quiz=quiz, ques=ques)
    question.save()

    answer = models.QuizAns(quiz=quiz, ques=question, answer=ans)
    answer.save()

    return redirect(f'/addquestion/{pk}')

def organize(request):
    quizes = models.Quiz.objects.all()

    if request.method == "POST":
        if request.POST['quiz_name'] == '' or request.POST['quiz_state'] == '' or request.POST['quiz_cat'] == '' or request.POST['time'] == '':
            return redirect('/organize_event/')
        name = request.POST['quiz_name']
        state = request.POST['quiz_state']
        cat = request.POST['quiz_cat']
        time = request.POST['time']

        quiz = models.Quiz(quiz_name=name, quiz_status=state, quiz_cat=cat, time=time)
        quiz.save()

    dict = {'quizes':quizes}
    
    return render(request, 'organize.html', context=dict)
