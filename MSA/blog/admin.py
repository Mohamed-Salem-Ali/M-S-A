from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date')
    ordering = ('-date',)

admin.site.register(Post, PostAdmin)