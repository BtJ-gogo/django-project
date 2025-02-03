from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "author", "body"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["author"].required = True
        self.fields["category"].required = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "body"]
