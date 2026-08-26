from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    image = models.ImageField(
        upload_to='posts/'
    )

    caption = models.TextField(
        max_length=500,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='liked_posts'
    )

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.TextField(
        max_length=300
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user.username}: {self.text[:30]}'