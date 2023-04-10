from django import forms
from posts.models import Post


class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'pub_date', 'profile']
