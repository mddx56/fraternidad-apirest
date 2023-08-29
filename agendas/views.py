from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import (
    EstadoDeudaSerializer,
    TipoEventoSerializer,
    EstadoReservaSerializer,
    AgendaSerializer,
    DeudaSerializer,
#    DetalleDeudaSerializer,
    PagoSerializer,
    QrSerializer,
    TurnoSerializer,
    UserTurnoSerializer,
    MensualidadSerializer,
    ExtraordinariaSerializer,
    DeudaExtraordinariaSerializer,
)

from .models import (
    EstadoDeuda,
    TipoEvento,
    EstadoReserva,
    Agenda,
    Deuda,
    #DetalleDeuda,
    Pago,
    Qr,
    Turno,
    UserTurno,
    Mensualidad,
    Extraordinaria,
    DeudaExtraordinaria,
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

"""
class DetalleDeudaView(viewsets.ModelViewSet):
    serializer_class = DetalleDeudaSerializer
    queryset = DetalleDeuda.objects.all()
"""

class PagoView(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()


class QrView(viewsets.ModelViewSet):
    serializer_class = QrSerializer
    queryset = Qr.objects.all()


class TurnoView(viewsets.ModelViewSet):
    serializer_class = TurnoSerializer
    queryset = Turno.objects.all()


class UserTurnoView(viewsets.ModelViewSet):
    serializer_class = UserTurnoSerializer
    queryset = UserTurno.objects.all()


class MensualidadView(viewsets.ModelViewSet):
    serializer_class = MensualidadSerializer
    queryset = Mensualidad.objects.all()


class ExtraordinariaView(viewsets.ModelViewSet):
    serializer_class = ExtraordinariaSerializer
    queryset = Extraordinaria.objects.all()


class DeudaExtraordinariaView(viewsets.ModelViewSet):
    serializer_class = DeudaExtraordinariaSerializer
    queryset = DeudaExtraordinaria.objects.all()


from rest_framework import generics


class DeudasPorClienteListView(generics.ListAPIView):
    serializer_class = DeudaSerializer

    def get_queryset(self):
        user_id = self.kwargs["id"]
        return Deuda.objects.filter(user=user_id).order_by("estado_deuda")


"""class AgendaAllView(APIView):
    def get(self, request):
        queryset = Agenda.objects.all()
        serializer = AgendaSerializer(queryset, many=True)
        return Response(serializer.data)"""
