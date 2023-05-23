from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Author, Blog, AirBlog
from .permissions import AuthorOrReadOnly, IsAuth
from .serializers import AuthorSr, AirBlogSerializer, BlogSerializer


class AuthorDetailView(APIView):
    permission_classes = (AuthorOrReadOnly,)

    @staticmethod
    def get(request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            au = AuthorSr(Author.objects.get(pk=pk))
        except:
            return Response({'error': 'страница не найдена'})
        return Response({'author': au.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'ошибка нет id '})

        try:
            instance = Author.objects.get(pk=pk)
        except:
            return Response({'error': 'объект не найден'})

        author_sr = AuthorSr(data=request.data, instance=instance)
        author_sr.is_valid(raise_exception=True)
        author_sr.save()
        return Response({'author': author_sr.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'ошибка нет id '})
        try:
            au = Author.objects.get(pk=pk)
            au.delete()
        except:
            return Response({'author': 'объект не найден'})
        return Response({'author': 'объект удален'}, status=status.HTTP_204_NO_CONTENT)


class AuthorView(APIView):
    permission_classes = (IsAuth,)

    @staticmethod
    def get(request):
        au = AuthorSr(Author.objects.all(), many=True)
        return Response({'author': au.data}, status=status.HTTP_200_OK)

    def post(self, request):
        au = AuthorSr(data=request.data)
        au.is_valid(raise_exception=True)
        au.save()
        return Response(au.validated_data, status=status.HTTP_201_CREATED)


class BlogView(APIView):
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuth,)

    def get(request, *args, **kwargs):
        blog = BlogSerializer(Blog.objects.all(), many=True)
        return Response({'blog': blog.data})

    def post(self, request, *args, **kwargs):
        blog = BlogSerializer(data=request.data)
        blog.is_valid(raise_exception=True)
        blog.save()
        return Response(blog.validated_data, status=status.HTTP_201_CREATED)


class BlogDetailView(APIView):
    permission_classes = (AuthorOrReadOnly,)

    @staticmethod
    def get(request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            blog = BlogSerializer(Blog.objects.get(pk=pk))
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

        blog = BlogSerializer(data=request.data, instance=instance)
        blog.is_valid(raise_exception=True)
        blog.save()

        return Response({'blog': blog.data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id  не найден'})

        is_deleted, _ = Blog.objects.filter(pk=pk).delete()

        # instance.delete()
        if not is_deleted:
            return Response({'error': 'не найден'})

        return Response({'blog': 'объект удален из базы данных'}, status=status.HTTP_204_NO_CONTENT)


class AirBlogView(APIView):
    permission_classes = (IsAuth,)

    @staticmethod
    def get(request):
        air_blog = AirBlogSerializer(AirBlog.objects.all(), many=True)
        return Response({'air_blog': air_blog.data}, status=status.HTTP_200_OK)

    def post(self, request):
        air_blog = AirBlogSerializer(data=request.data)
        air_blog.is_valid(raise_exception=True)
        air_blog.save()
        return Response(air_blog.validated_data, status=status.HTTP_201_CREATED)


class AirBlogDetailView(APIView):
    permission_classes = (AuthorOrReadOnly,)

    @staticmethod
    def get(request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            instance = AirBlog.objects.get(pk=pk)
        except:
            return Response({'error': 'страница не найдена'})

        return Response({'air_detail': instance.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id не найден'})

        try:
            instance = AirBlog.objects.get(pk=pk)
        except:
            return Response({'error': 'страница не найдена'})

        air = AirBlogSerializer(data=request.data, instance=instance)
        air.is_valid()
        return Response({'air_update': air.data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'id не найден'})
        try:
            instance = AirBlog.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'страница не найдена'})

        return Response({'air_delete': 'страница удалена'}, status=status.HTTP_204_NO_CONTENT)
