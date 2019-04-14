from django.contrib import admin
from django.forms import Textarea
from django.db import models
from blog.models import Post, PostCategory, Comment

# Register your models here.
@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin) : 
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin) : 
        list_display = (
                        'title', 
                        'category', 
                        'published', 
                        'text',
                        'created_at',
                        'comments_count',
                        )

        list_filter = (
            'category__name', 
            'published',
        )

        autocomplete_fields = ['category']

        formfield_overrides = {
            models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})}
        }

        def comments_count(self, obj) : 
            # Pour chaque post cb de commentaires ont été crée
            return Comment.objects.filter(post=obj).count()

        comments_count.short_description='Comments'