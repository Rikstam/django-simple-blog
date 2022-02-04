from django.contrib import admin
from .models import Tag, CustomUser, Author, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """Customise the admin panel for a Post"""
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    pre_populated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)