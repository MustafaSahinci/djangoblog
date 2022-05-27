from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin  


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_one")
    summernote_fields = ("content")
    list_display = ("title", "slug", "status", "created_one")
    search_fields = ("title", "content")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_one", "approved")
    list_filter = ("approved", "created_one")
    search_fields = ("name", "email","body")
    actions = ["approve_comments"]


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)