from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Video


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EDITOR, 'Editor'),
        (VIEWER, 'Viewer'),
    ]

    role = serializers.ChoiceField(choices=ROLE_CHOICES, default=VIEWER)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'email', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_url']