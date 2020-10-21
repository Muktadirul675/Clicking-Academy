from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    post = models.TextField()
    user_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + " "+ self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    comment = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    inst = models.CharField(max_length=200)
    dscrb = models.TextField()
    category = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.name + self.category


class EventRule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rules')
    rule = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.event) +" ----> "+ self.rule


class Quiz(models.Model):
    quiz_status = models.CharField(max_length=100)
    quiz_name = models.CharField(max_length=300)
    quiz_cat = models.CharField(max_length=300)
    time = models.IntegerField()

    def __str__(self):
        return f"{self.quiz_name} {self.quiz_status} {self.quiz_cat}"

class QuizQue(models.Model):
    ques = models.TextField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ques}"

class QuizAns(models.Model):
    ques = models.ForeignKey(QuizQue, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)
    quiz = models.ForeignKey(Quiz, related_name='answers', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{str(self.ques)} {self.answer} "


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='result', on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    result = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user} {self.result}"
