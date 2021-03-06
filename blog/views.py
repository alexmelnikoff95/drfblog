from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, Blog
from .permissions import IsAdminUser, AuthorOrReadOnly
from .serializers import BlogSerializers, AuthorSerializers, AuthorSr

from rest_framework.permissions import IsAuthenticated


class AuthorDetailView(APIView):
    permission_classes = (AuthorOrReadOnly,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            au = AuthorSr(Author.objects.get(pk=pk))
        except:
            return Response({'error': 'страница не найдена'})
        return Response({'author': au.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'ошибка нет id '})

        try:
            instance = Author.objects.get(pk=pk)
        except:
            return Response({'error': 'объект не найден'})

        serializer = AuthorSr(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'author': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'ошибка нет id '})
        try:
            au = Author.objects.get(pk=pk)
            au.delete()
        except:
            return Response({'author': 'объект не найден'})
        return Response({'author': 'объект удален'})


class AuthorView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        au = AuthorSerializers(Author.objects.all(), many=True)
        return Response({'author': au.data})

    def post(self, request):
        au = AuthorSerializers(data=request.data)
        au.is_valid(raise_exception=True)
        au.save()
        return Response(au.validated_data)


class BlogView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        blog = BlogSerializers(Blog.objects.all(), many=True)
        return Response({'blog': blog.data})

    def post(self, request):
        blog = BlogSerializers(data=request.data)
        blog.is_valid(raise_exception=True)
        blog.save()
        return Response(blog.validated_data)


class BlogDetailView(APIView):
    permission_classes = (AuthorOrReadOnly,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            blog = BlogSerializers(Blog.objects.get(pk=pk))
        except:
            return Response({'error': 'страница не найдена'})
        return Response({'author': blog.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id  не найден'})
        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({'error': 'страница не найдена'})

        blog = BlogSerializers(data=request.data, instance=instance)
        blog.is_valid(raise_exception=True)
        blog.save()
        return Response({'blog': blog.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id  не найден'})
        try:
            instance = Blog.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'объект не найден'})

        return Response({'blog': 'объект удален из базы данных'})
