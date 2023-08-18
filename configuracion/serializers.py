from rest_framework import serializers
from .models import Fraternidad, Medio


class FraternidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraternidad
        fields = "__all__"


class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = "__all__"
