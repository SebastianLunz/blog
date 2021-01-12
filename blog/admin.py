from django.contrib import admin
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "title_tag",
        "author",
        "post_date",
        "category",
    ]
    list_filter = [
        "title",
        "title_tag",
        "author",
        "post_date",
        "category",
    ]
    search_fields = [
        "title",
        "title_tag",
        "author",
        "post_date",
        "category",
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "post",
        "name",
        "date_added",
    ]
    list_filter = [
        "post",
        "name",
        "date_added",
    ]
    search_fields = list_filter = [
        "post",
        "name",
        "date_added",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ["name".lower()]
    search_fields = ["name".lower()]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
