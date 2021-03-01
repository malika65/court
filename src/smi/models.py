from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Category(models. Model):
    title =  models.CharField(max_length=200, verbose_name = 'Заголовок')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def _str(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Заголовок')
    body = QuillField(verbose_name = 'Тело поста')
    category = models.ManyToManyField(Category, related_name = 'category', verbose_name = 'Категории')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
    def __str__(self):
        return self.title



class Region(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Область')
    
    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=200,verbose_name='Имя пользователя')
    user_email = models.EmailField(max_length=254,verbose_name='Email пользователя')
    user_comment = models.TextField(max_length=1500,verbose_name='Комментарий пользователя')


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'




    def __str__(self):
        return self.user_name
