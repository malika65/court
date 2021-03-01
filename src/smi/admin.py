from django.contrib import admin
from .models import Post, Tag, Vacancy

# Register your models here.

# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Vacancy)

@admin.register(Post)
class QuillPostAdmin(admin.ModelAdmin):
    pass



