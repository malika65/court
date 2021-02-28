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

