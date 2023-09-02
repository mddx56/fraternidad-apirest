from rest_framework import serializers
from .models import Cumpleanio, Fraternidad, Medio


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


class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = "__all__"
