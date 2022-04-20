from django.urls import path

from blog.views import BlogView, AuthorView, AuthorDetailView, BlogDetailView

urlpatterns = [
    path('list_blog', BlogView.as_view(), name='blog'),
    path('list_author', AuthorView.as_view(), name='author'),
    path('list_author/<int:pk>', AuthorView.as_view(), name='author'),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]
