from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Posts(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.author.username} -- {self.title} -- {self.created_at}'


