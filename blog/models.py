from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

'''

comments
add post

'''


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000, help_text='your description')
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date']


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=2000, help_text='your bio')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author', args=[str(self.id)])

    class Meta:
        ordering = ['user', 'bio']


class Comment(models.Model):
    description = models.TextField(1000, help_text='Enter comment about blog here.')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        len_default = 75
        if len(self.description) > len_default:
            out_title = self.description[:len_default] + '...'
        else:
            out_title = self.description
        return out_title

    class Meta:
        ordering = ['post_date']
