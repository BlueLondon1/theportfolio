from django.contrib import admin
from django.db import models
from django.forms import Textarea

# Register your models here.
from appfolio.models import PostCategory, Post

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'published',
        'created_at',
    )

    list_filter = (
        'published',
    )

    formfield_overrides = {
        models.TextField: {'widget' : Textarea(attrs={'rows': 20, 'cols': 90})}
    }
