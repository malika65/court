from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Post(models.Model):
    body = QuillField()

class Tag(models.Model):
    tags = models.CharField(max_length=200)

