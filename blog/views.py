from django.shortcuts import render
from .models import Post, Author, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    num_author = Author.objects.count()
    num_post = Post.objects.all().count()
    num_comment = Comment.objects.all().count()
    return render(request, 'index.html', context={'num_author': num_author, 'num_post': num_post,
                                                  'num_comment': num_comment})


class AuthorsList(generic.ListView):
    model = Author
    paginate_by = 10


class BlogsList(generic.ListView):
    model = Post
    paginate_by = 10


class AuthorDetail(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/author_detail.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(Author, pk=id)
        return Post.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(Author, pk=self.kwargs['pk'])
        return context


class BlogDetail(generic.DetailView):
    model = Post


@login_required(login_url='/accounts/login/')
def create_comment(request, pk):
    post_url = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            return redirect('blog', pk=pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment.html', {'form': form, 'post_url': post_url})
