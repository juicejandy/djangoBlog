from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.timezone import now

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='Lorem ipsum')
    pub_date = models.DateTimeField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.text