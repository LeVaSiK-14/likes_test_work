from django.db import models
from posts.models import Posts
from django.contrib.auth import get_user_model

User = get_user_model()


class Likes(models.Model):

    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='like')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Лайки"
        verbose_name_plural = "Лайк"

    def __str__(self):
        return f"{self.author.username} -- {self.post.title} -- {self.created_at}"


class DisLikes(models.Model):

    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='dislike')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Дизлайки"
        verbose_name_plural = "Дизлайк"

    def __str__(self):
        return f"{self.author.username} -- {self.post.title} -- {self.created_at}"
