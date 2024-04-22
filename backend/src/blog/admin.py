from django.contrib import admin
from src.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["overview"]}
