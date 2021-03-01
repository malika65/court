from django.contrib import admin
from .models import Post, Category,Region,Comments

# Register your models here.

# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Region)

admin.site.register(Comments)


@admin.register(Post)
class QuillPostAdmin(admin.ModelAdmin):
    pass

