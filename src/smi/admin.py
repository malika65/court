from django.contrib import admin
from .models import Post, Category,Region,Comments,Vacancy


# Register your models here.

admin.site.register(Category)
admin.site.register(Region)

admin.site.register(Comments)

admin.site.register(Vacancy)

@admin.register(Post)
class QuillPostAdmin(admin.ModelAdmin):
    pass



