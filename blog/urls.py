from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bloggers/$', views.AuthorsList.as_view(), name='bloggers'),
    url(r'^blogs/$', views.BlogsList.as_view(), name='blogs')
]
