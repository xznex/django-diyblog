from django.shortcuts import render
from .models import Post, Author, Comment
from django.views import generic


def index(request):
    num_author = Author.objects.count()
    num_post = Post.objects.all().count()
    num_comment = Comment.objects.all().count()
    return render(request, 'index.html', context={'num_author': num_author, 'num_post': num_post,
                                                  'num_comment': num_comment})


class AuthorsList(generic.ListView):
    model = Author
    # paginate_by = 10


class BlogsList(generic.ListView):
    model = Post
    # paginate_by = 10
