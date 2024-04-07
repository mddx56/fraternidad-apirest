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
from accounts.models import UserAccount

from .serializer import (
    TipoEventoSerializer,
    AgendaSerializer,
    PagoSerializer,
    QrSerializer,
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
    ListPagoSerializer,
    ListDetallePagoMensualidadSerializer,
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


class ListPagosView(APIView):

    def get(self, request, ci, format=None):
        try:
            frater = UserAccount.objects.filter(username=ci).first()
            if frater:
                detallalles = DetallePagoMensualidad.objects.filter(pago__user=frater)
                serializer = ListDetallePagoMensualidadSerializer(
                    detallalles, many=True
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)


class ListExtraordinariaView(APIView):

    def get(self, request, id_extra, ci, format=None):
        try:
            frater = UserAccount.objects.filter(username=ci).first()
            extraodinaria = Extraordinaria.objects.get(id=id_extra)
            if frater:
                pagos = Pago.objects.filter(user=frater)
                detallalles = DetallePagoMensualidad.objects.filter(pago__user=frater)
                serializer = ListDetallePagoMensualidadSerializer(
                    detallalles, many=True
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)
