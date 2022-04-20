from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='имя')
    last_name = models.CharField(max_length=255, verbose_name='фамилия')
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return f'{self.last_name} - {self.first_name}'


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='название блога')
    text = models.TextField(verbose_name='текст блога')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return self.title
