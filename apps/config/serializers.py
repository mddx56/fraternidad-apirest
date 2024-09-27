from rest_framework import serializers
from .models import (
    Cumpleanio,
    Fraternidad,
    MediaImage,
    MediaVideo,
    Articulo,
    Cronograma,
    Actividad,
    DiaSemana,
    Horario,
)


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


class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronograma
        fields = "__all__"


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"


class DiaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaSemana
        fields = "__all__"


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = "__all__"
