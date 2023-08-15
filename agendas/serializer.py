from rest_framework import serializers


from .models import (
    EstadoReserva,
    TipoEvento,
    EstadoDeuda,
    Agenda,
    Deuda,
    DetalleDeuda,
    Pago,
    Qr,
    Turno,
    UserTurno
)


class EstadoReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoReserva
        fields = "__all__"


class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = "__all__"


class EstadoDeudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDeuda
        fields = "__all__"


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = "__all__"


class DeudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deuda
        fields = "__all__"


class DetalleDeudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleDeuda
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