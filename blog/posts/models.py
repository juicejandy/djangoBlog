from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField
    pub_date = models.DateTimeField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.CharField(max_length=250)
    user_comment = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text



