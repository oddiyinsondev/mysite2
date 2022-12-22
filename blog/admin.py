from django.contrib import admin
from .models import Post, Category, CommentPost, Contact

admin.site.register(CommentPost)
admin.site.register(Contact)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'author', 'created', 'publish', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug': ('title', )  }
    ordering = ('status', 'publish')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('title',)

