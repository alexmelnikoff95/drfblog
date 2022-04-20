from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, Blog
from .serializers import BlogSerializers, AuthorSerializers, AuthorSr

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class AuthorDetailView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            au = AuthorSr(Author.objects.get(pk=pk))
        except:
            return Response({'error': 'страница не найдена'})
        return Response({'author': au.data})


class AuthorView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # def post(self, request):
    #     # new = Author.objects.create(
    #     #     first_name=request.data['first_name'],
    #     #     last_name=request.data['last_name'])
    #     # return Response({'author': model_to_dict(new)})
    #     # return Response({'author': AuthorSerializers(new).data})
    #
    #     au = AuthorSerializers(data=request.data)
    #
    #     au.is_valid(raise_exception=True)
    #     return Response(au.validated_data)

    def get(self, request):
        au = AuthorSerializers(Author.objects.all(), many=True)
        # sr = AuthorResponseSerializers(data={'author': au.data})
        # au.is_valid(raise_exception=True)
        return Response({'author': au.data})

    def post(self, request):
        au = AuthorSerializers(data=request.data)
        au.is_valid(raise_exception=True)
        au.save()
        return Response(au.validated_data)

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


class BlogView(APIView):

    def get(self, request):
        blog_sr = BlogSerializers(Blog.objects.all(), many=True)
        sr = BlogSerializers(data={'blog': blog_sr.data})
        sr.is_valid(raise_exception=True)
        return Response(data=sr.validated_data)

    def post(self, request):
        sr = BlogSerializers(data=request.data)
        sr.is_valid(raise_exception=True)
        sr.save()
        return Response({'blog': sr.data})
