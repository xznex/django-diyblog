from django.contrib import admin
from .models import Post, BlogAuthor, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_date', 'title', 'author')
    inlines = [CommentInline]


@admin.register(BlogAuthor)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
