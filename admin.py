from django.contrib import admin
from .models import Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'id', 'image', 'slug', 'author', 'status_color')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, AuthorAdmin)