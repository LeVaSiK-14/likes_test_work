from django.contrib import admin
from likes.models import Likes, DisLikes

class LikesAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']

admin.site.register(Likes, LikesAdmin)

class DisLikesAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']

admin.site.register(DisLikes, DisLikesAdmin)
