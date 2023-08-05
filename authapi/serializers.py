from rest_framework import serializers
#from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import (
    Notificacion,
    Token
)

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = "__all__"

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"