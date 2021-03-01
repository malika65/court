from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Заголовок')
    body = QuillField(verbose_name = 'Тело поста')
    tags = models.ManyToManyField(Tag, related_name = 'post', verbose_name = 'Теги')
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Заголовок')
    body = models.TextField(max_length=1500, verbose_name = 'Тело поста')
    contact = models.CharField(max_length=100, null=True, blank=True, verbose_name='Контакты')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


