from django.contrib import admin
from django.urls import path
from . import views

app_name = 'academy'

urlpatterns = [
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),    
    path("blog/",views.blog, name="blog"),
    path("blog/members/",views.blog_members, name="blog_members"),
    path("signup_page/",views.signup_page, name="signup_page"),
    path("signup/",views.signup, name="signup"),
    path("login_page/",views.login_page, name="login_page"),
    path("login/",views.user_login, name="login"),
    path("logout/",views.user_logout, name="logout"),
    path('activities/', views.activity, name="activity"),
    path('blog_post/', views.blog_post, name="blog_post"),
    path('add_blog_post/', views.addpost, name="addpost"),
    path('delete_blog_post/<int:pk>/', views.del_post, name="delete_post"),
    path('post/<int:pk>', views.post, name="post"),
    path('post/<int:pk>/add_comment', views.add_comment, name="add_comment"),
    path('blog/events/', views.event, name="event"),
    path('blog/events/<int:pk>', views.seeevent, name="seeevent"),
    path('blog/events/del_post/<int:pk>',views.del_event, name="del_event"),
    path('quizes/', views.quizes, name='quizes'),
    path('participate/<str:state>/<int:pk>/', views.part, name='part'),
    path('result/', views.result, name="result"),
    path('result/<int:pk>/', views.result_event, name='result_event'),
    path('addquestion/<int:pk>/', views.addquestion, name="addquestion"),
    path('organize_event/', views.organize, name='organize'),
    path('addquestion_fun/', views.addquestion_fun, name="addquestion_fun"),
]
