from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='followers'
    )

    @property
    def unread_notifications_count(self):
        return self.notifications.filter(is_read=False).count()

    def __str__(self):
        return self.username