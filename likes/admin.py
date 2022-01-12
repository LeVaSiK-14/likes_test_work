from django.contrib import admin
from likes import models


class LikesAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']


class DisLikesAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']


admin.site.register(models.DisLikes, DisLikesAdmin)
admin.site.register(models.Likes, LikesAdmin)
