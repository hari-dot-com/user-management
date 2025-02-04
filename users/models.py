from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EDITOR, 'Editor'),
        (VIEWER, 'Viewer'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=VIEWER)

    # Fix related_name clashes
    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customuser_permissions', blank=True
    )

    def __str__(self):
        return self.username

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()  # This will store the URL of the video

    def __str__(self):
        return self.title