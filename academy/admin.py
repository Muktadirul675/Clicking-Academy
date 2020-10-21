from django.contrib import admin
from .models import  Comment, Post, EventRule, Event, Quiz, QuizAns, QuizQue, Result

# Register your models here.

# admin.site.register(Post)
admin.site.register((Post,Comment,EventRule, Event, Quiz, QuizAns, QuizQue, Result))
