from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from blog.models import Author, Blog

UserModel = get_user_model()


class TestAuthorView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('author')

    def test_api_response(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_serializer(self):
        pass


# @patch('blog.permissions.AuthorOrReadOnly.has_permission', side_effect=lambda *args, **kwargs: True)
class TestBlogView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('blog')
        # c = UserModel.objects.create_user(username='user1')
        b = User.objects.create(username='user2', UserModel='user2')
        print(b)
        b = Author.objects.create(first_name='alex', last_name='123', user_id=1, user='user2')
        # a = Blog.objects.create(title='test', text='test_text', author='alex')
        print(b)

    def test_api_response(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_serializer(self):
        pass
