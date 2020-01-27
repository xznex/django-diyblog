from django.shortcuts import render
from .models import Post, BlogAuthor, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
# from django.shortcuts import redirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


def index(request):
    num_author = BlogAuthor.objects.count()
    num_post = Post.objects.all().count()
    num_comment = Comment.objects.all().count()
    return render(request, 'index.html', context={'num_author': num_author, 'num_post': num_post,
                                                  'num_comment': num_comment})


class AuthorsList(generic.ListView):
    model = BlogAuthor
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
        target_author = get_object_or_404(BlogAuthor, pk=id)
        return Post.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context


class BlogDetail(generic.DetailView):
    model = Post


# @login_required(login_url='/accounts/login/')
# def create_comment(request, pk):
#     post_url = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#
#         if form.is_valid():
#             return redirect(reverse('blog', kwargs={'pk': pk}))
#
#     else:
#         form = CommentForm()
#
#     return render(request, 'blog/comment_form.html', {'form': form, 'post_url': post_url})


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description', ]

    def get_context_data(self, **kwargs):
        context = super(CreateComment, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super(CreateComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog', kwargs={'pk': self.kwargs['pk']})
