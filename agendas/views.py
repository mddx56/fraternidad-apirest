from rest_framework import viewsets
from .serializer import (
    EstadoDeudaSerializer,
    TipoEventoSerializer,
    EstadoReservaSerializer,
    AgendaSerializer,
    DeudaSerializer,
    DetalleDeudaSerializer,
    PagoSerializer,
    QrSerializer,
)
from .models import (
    EstadoDeuda,
    TipoEvento,
    EstadoReserva,
    Agenda,
    Deuda,
    DetalleDeuda,
    Pago,
    Qr,
)


class EstadoDeudaView(viewsets.ModelViewSet):
    serializer_class = EstadoDeudaSerializer
    queryset = EstadoDeuda.objects.all()

class TipoEventoSerializerView(viewsets.ModelViewSet):
    serializer_class = TipoEventoSerializer
    queryset = TipoEvento.objects.all()

class EstadoReservaView(viewsets.ModelViewSet):
    serializer_class = EstadoReservaSerializer
    queryset = EstadoReserva.objects.all()

class AgendaView(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()

class DeudaView(viewsets.ModelViewSet):
    serializer_class = DeudaSerializer
    queryset = Deuda.objects.all()

class DetalleDeudaView(viewsets.ModelViewSet):
    serializer_class = DetalleDeudaSerializer
    queryset = DetalleDeuda.objects.all()

class PagoView(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()

class QrView(viewsets.ModelViewSet):
    serializer_class = QrSerializer
    queryset = Qr.objects.all()