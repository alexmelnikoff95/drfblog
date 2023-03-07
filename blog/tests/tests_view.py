import json
from unittest.mock import patch

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from blog.models import Author, Blog, AirBlog


@patch('blog.permissions.IsAuth.has_permission', side_effect=lambda *args, **kwargs: True)
class TestAuthorView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('author')

    def test_get(self, *args, **kwargs):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self, *args, **kwargs):
        data = {
            "first_name": "Alexander",
            "last_name": "Melnikov",
        }

        json_data = json.dumps(data)

        response = self.client.post(self.url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_serializer(self, *args, **kwargs):
        pass


@patch('blog.permissions.AuthorOrReadOnly.has_permission', side_effect=lambda *args, **kwargs: True)
class TestAuthorDetailView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='name1', last_name='name2')
        cls.url = reverse('author_detail', args=(author.id,))

    def test_get(self, *args, **kwargs):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self, *args, **kwargs):
        dump = json.dumps({'first_name': 'jon',
                           'last_name': 'snow'})

        response = self.client.put(self.url, data=dump, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self, *args, **kwargs):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

    def test_serializer(self, *args, **kwargs):
        pass


@patch('blog.permissions.IsAuth.has_permission', side_effect=lambda *args, **kwargs: True)
class TestBlogView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('blog')

    def test_get(self, *args, **kwargs):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self, *args, **kwargs):
        dump = json.dumps({'title': 'title1',
                           'text': 'text1'})
        response = self.client.post(self.url, data=dump, content_type='application/json')
        self.assertEqual(response.status_code, 201)


@patch('blog.permissions.AuthorOrReadOnly.has_permission', side_effect=lambda *args, **kwargs: True)
class TestBlogDetailView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        blog = Blog.objects.create(title='title1', text='text1')
        cls.url = reverse('blog_detail', args=(blog.id,))

    def test_put(self, *args, **kwargs):
        dump = json.dumps({
            'title': 'title2',
            'text': 'text2'
        })
        response = self.client.put(self.url, data=dump, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self, *args, **kwargs):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)


@patch('blog.permissions.IsAuth.has_permission', side_effect=lambda *args, **kwargs: True)
class AirTestView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test1')
        cls.url = reverse('air')

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_get(self, *args, **kwargs):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self, *args, **kwargs):
        data = {
            "title": "test1",
            "text": "text1"
        }
        json_dump = json.dumps(data)
        response = self.client.post(self.url, data=json_dump, content_type='application/json')
        self.assertEqual(response.status_code, 201)


@patch('blog.permissions.AuthorOrReadOnly.has_permission', side_effect=lambda *args, **kwargs: True)
class AirDetailTestView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        air = AirBlog.objects.create(title='название', text='текст')
        cls.url = reverse('air_detail', args=(air.id,))

    def test_put(self, *args, **kwargs):
        data = {
            'title': '123',
            'text': '223'
        }
        dump_data = json.dumps(data)
        response = self.client.put(self.url, data=dump_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self, *args, **kwargs):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
