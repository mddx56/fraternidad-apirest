from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import UserAccount
from rest_framework.decorators import api_view
import datetime
from .serializer import dato_to_moth

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

from .serializer import (
    TipoEventoSerializer,
    AgendaSerializer,
    PagoSerializer,
    QrSerializer,
    TurnoSerializer,
    UserTurnoSerializer,
    MensualidadSerializer,
    ExtraordinariaSerializer,
    GestionSerializer,
    DetallePagoEventoSerializer,
    DetallePagoExtraordianriaSerializer,
    DetallePagoMensualidadSerializer,
    GrupoTurnoSerializer,
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


def is_valido_date(mes, anio):
    fecha_actual = datetime.datetime.now()
    anio_actual = fecha_actual.year
    mes_actual = fecha_actual.month
    return anio < anio_actual or (anio == anio_actual and mes <= mes_actual)


def frater_pay_date(ci, mes, anio):
    frater = UserAccount.objects.filter(username=ci).first()
    detalle = DetallePagoMensualidad.objects.filter(
        pago__user=frater, mensualidad__gestion__anio=anio
    )

    result = detalle.filter(mensualidad__mes=mes).first()

    ok = True if result else False
    return ok


@api_view(["GET"])
def ListMensualidadDeudaView(request, ci):
    try:
        # frater = UserAccount.objects.filter(username=ci).first()

        gestions = Gestion.objects.all().order_by("anio")

        deudas = []

        for gg in gestions:
            anio = gg.anio

            mensualidades = Mensualidad.objects.filter(gestion=gg).order_by("mes")
            for mensu in mensualidades:
                mes = mensu.mes
                if not frater_pay_date(ci, mes, anio) and is_valido_date(mes, anio):
                    deudas.append(
                        {
                            "mes": dato_to_moth(mensu.mes),
                            "costo": mensu.costo,
                            "gestion": gg.anio,
                        }
                    )

        mensualidades
        suma = sum([num["costo"] for num in deudas])

        return Response({"deudas": deudas, "total": suma}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def ListDeudaExtraordinaria(request, ci):
    frater = UserAccount.objects.filter(username=ci).first()
    extraordinarias = Extraordinaria.objects.all()

    deudax = []

    sum_saldo = 0

    for extra in extraordinarias:
        sum_saldo = 0
        detalles = DetallePagoExtraordianria.objects.filter(
            pago__user=frater, extraordinaria=extra
        )
        total_extra = extra.monto
        extra = extra.to_json()
        for detalle in detalles:
            sum_saldo = sum_saldo + detalle.pago.monto_pagado
        deuda = total_extra - sum_saldo
        deudax.append({"extraordinaria": extra, "saldo": sum_saldo, "deuda": deuda})

    return Response(deudax, status=status.HTTP_200_OK)
