from django.contrib import admin
from posts.models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ["author", 'created_at', 'likes', 'dislikes']

admin.site.register(Posts, PostsAdmin)
