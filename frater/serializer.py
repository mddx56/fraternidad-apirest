from rest_framework import serializers
from .models import (
    Fraternidad,
    Cumpleanio,
)


class FraternidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraternidad
        fields = "__all__"

class CumpleanioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cumpleanio
        fields = "__all__"