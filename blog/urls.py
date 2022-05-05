from django.urls import path

from blog.views import BlogView, AuthorView, AuthorDetailView, BlogDetailView

urlpatterns = [
    path('blog_list', BlogView.as_view(), name='blog'),
    path('author_list', AuthorView.as_view(), name='author'),
    path('author_list/<int:pk>', AuthorView.as_view(), name='author'),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]
