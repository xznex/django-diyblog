from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

'''

author > get_abs_url
post > get_abs_url
comment

'''


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000, help_text='your description')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=2000, help_text='your bio')

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    description = models.TextField(1000, help_text='your comment')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        len_default = 75
        if len(self.description) > len_default:
            out_title = self.description[:len_default] + '...'
        else:
            out_title = self.description
        return out_title
