from rest_framework import serializers


from .models import (
    TipoEvento,
    Agenda,
    Pago,
    Qr,
    Turno,
    TurnoPl,
    UserTurno,
    Mensualidad,
    Extraordinaria,
    DeudaExtraordinaria,
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


class DeudaExtraordinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeudaExtraordinaria
        fields = "__all__"


class TurnoPlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnoPl
        fields = "__all__"
