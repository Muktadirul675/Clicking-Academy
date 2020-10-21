from django import forms
from .models import Event


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = "__all__"

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name','comment')


class EventForm(forms.ModelForm):
    class  Meta:
        model = Event
        fields = "__all__"
