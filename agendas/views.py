from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

from .serializer import (
    TipoEventoSerializer,
    AgendaSerializer,
    PagoSerializer,
    QrSerializer,
    TurnoPlSerializer,
    TurnoSerializer,
    UserTurnoSerializer,
    MensualidadSerializer,
    ExtraordinariaSerializer,
    DeudaExtraordinariaSerializer,
    GestionSerializer,
    DetallePagoEventoSerializer,
    DetallePagoExtraordianriaSerializer,
    DetallePagoMensualidadSerializer,
    GrupoTurnoSerializer,
)


class GestionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = GestionSerializer
    queryset = Gestion.objects.all()


class DetallePagoEventoView(viewsets.ModelViewSet):
    serializer_class = DetallePagoEventoSerializer
    queryset = DetallePagoEvento.objects.all()


class DetallePagoExtraordianriaView(viewsets.ModelViewSet):
    serializer_class = DetallePagoExtraordianriaSerializer
    queryset = DetallePagoExtraordianria.objects.all()


class DetallePagoMensualidadView(viewsets.ModelViewSet):
    serializer_class = DetallePagoMensualidadSerializer
    queryset = DetallePagoMensualidad.objects.all()


class GrupoTurnoView(viewsets.ModelViewSet):
    serializer_class = GrupoTurnoSerializer
    queryset = GrupoTurno.objects.all()


class TipoEventoView(viewsets.ModelViewSet):
    serializer_class = TipoEventoSerializer
    queryset = TipoEvento.objects.all()


class AgendaView(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()


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


class TurnoPlView(viewsets.ModelViewSet):
    serializer_class = TurnoPlSerializer
    queryset = TurnoPl.objects.all()


"""
from rest_framework import generics

class DeudasPorClienteListView(generics.ListAPIView):
    serializer_class = DeudaSerializer

    def get_queryset(self):
        user_id = self.kwargs["id"]
        return Deuda.objects.filter(user=user_id).order_by("estado_deuda")
"""


class VerPagosView(APIView):
    # def get(self, request, pk):
    def get(self, request, *args, **kwargs):
        pass
        #pagos = Pago.objects.filte(user=request.user.id)
        #serializer = PagoSerializer(pagos, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)


# Usamos select_related() y prefetch_related() para optimizar la consulta
# resultado = ModeloA.objects.select_related('modelo_b').prefetch_related('modelo_b__modelo_c').get(pk=1)

# Ahora podemos acceder a los objetos relacionados de ModeloC
#  objetos_modelo_c = resultado.modelo_b.all()[0].modelo_c.all()
