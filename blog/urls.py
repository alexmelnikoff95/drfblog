from django.urls import path, include, re_path

from blog.views import BlogView, AuthorView, AuthorDetailView, BlogDetailView

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('blog_list', BlogView.as_view(), name='blog'),
    path('author_list', AuthorView.as_view(), name='author'),
    path('author_list/<int:pk>', AuthorView.as_view(), name='author'),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]
