from rest_framework import serializers
import calendar

from .models import (
    TipoEvento,
    Agenda,
    Pago,
    Qr,
    Turno,
    UserTurno,
    Mensualidad,
    Extraordinaria,
    GrupoTurno,
    Gestion,
    DetallePagoEvento,
    DetallePagoExtraordianria,
    DetallePagoMensualidad,
)


class GrupoTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoTurno
        fields = "__all__"


class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestion
        fields = "__all__"


class DetallePagoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePagoEvento
        fields = "__all__"


class DetallePagoExtraordianriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePagoExtraordianria
        fields = "__all__"


"""
    def create(self, validated_data):
        # Perform object-level validation
        if (
            validated_data["pago__monto_pagado"]
            <= validated_data["extraordinaria__monto"]
        ):
            raise serializers.ValidationError(
                "No puede exeder a el precio de la extraordinaria."
            )

        # Save the object
        return DetallePagoEventoSerializer.objects.create(**validated_data)
"""


class DetallePagoMensualidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePagoMensualidad
        fields = "__all__"


class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = "__all__"


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = "__all__"


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"


class QrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qr
        fields = "__all__"


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = "__all__"


class UserTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTurno
        fields = "__all__"


class MensualidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensualidad
        fields = "__all__"


class ExtraordinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extraordinaria
        fields = "__all__"


def dato_to_moth(number_moth):
    meses_en_espanol = [
        "",
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    calendar.month_name = meses_en_espanol
    return calendar.month_name[number_moth]


class ListDetallePagoMensualidadSerializer(serializers.ModelSerializer):
    mes = serializers.SerializerMethodField()
    gestion = serializers.SerializerMethodField()
    monto = serializers.SerializerMethodField()

    class Meta:
        model = DetallePagoMensualidad
        fields = "__all__"

    def get_mes(self, object):
        return dato_to_moth(object.mensualidad.mes)

    def get_gestion(self, object):
        return object.mensualidad.gestion.anio

    def get_monto(self, object):
        return object.mensualidad.costo


class ListPagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pago
        fields = "__all__"
