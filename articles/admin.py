from django.contrib import admin

from .models import Category, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    list_filter = ['title', 'created']
    search_fields = ['title', 'author']
admin.site.register(Article, ArticleAdmin)


admin.site.register(Category)
admin.site.register(Comment)