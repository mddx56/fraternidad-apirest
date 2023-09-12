from rest_framework import serializers
from .models import Cumpleanio, Fraternidad, MediaImage, MediaVideo, Articulo


class CumpleanioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cumpleanio
        fields = "__all__"


"""
class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = "__all__"


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"
"""


class FraternidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraternidad
        fields = "__all__"


class MediaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = "__all__"


class MediaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaVideo
        fields = "__all__"


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = "__all__"
