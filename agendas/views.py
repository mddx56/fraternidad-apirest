from django.db import transaction
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import UserAccount
from rest_framework.decorators import api_view
import datetime
from .serializer import dato_to_moth

from accounts.serializers import UserSerializer

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
    Cuota,
    DetallePagoExtraord,
    Extraord,
    FraterExtraord,
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
    CuotaInputSerializer,
    CuotaArraySerializer,
    CuotaSerializer,
    DetallePagoExtraord,
    FraterExtraord,
    Extraord,
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
    if not frater:
        return True
    detalle = DetallePagoMensualidad.objects.filter(
        pago__user=frater, mensualidad__gestion__anio=anio
    )

    result = detalle.filter(mensualidad__mes=mes).first()

    ok = True if result else False
    return ok


@api_view(["GET"])
def ListMensualidadDeudaView(request, ci):
    try:
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
                            "id": mensu.id,
                            "mes": dato_to_moth(mensu.mes),
                            "gestion": gg.anio,
                            "costo": mensu.costo,
                            "fecha": mensu.fecha,
                            "mensualidad": mensu.pk,
                        }
                    )

        mensualidades
        suma = sum([num["costo"] for num in deudas])

        return Response({"deudas": deudas, "total": suma}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def ListDeudaExtraordinaria(request, ci):
    frater = UserAccount.objects.get(username=ci)
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


@api_view(["GET"])
def ListFratersGroup(request, id):
    grupo = GrupoTurno.objects.get(pk=id)
    user_turno = UserTurno.objects.filter(grupo_turno=grupo).order_by("user__full_name")
    res = []
    for us in user_turno:
        res.append(us.user.to_json())
    return Response(res, status=status.HTTP_200_OK)


@api_view(["GET"])
def ListGroups(request):
    grupos = GrupoTurno.objects.all().order_by("nombre")
    res = []
    for gr in grupos:
        res_groups = []
        user_turno = UserTurno.objects.filter(grupo_turno=gr).order_by(
            "user__full_name"
        )
        for us in user_turno:
            res_groups.append(us.user.to_json())
        res.append({"nombre": gr.nombre, "fraternos": res_groups})

    return Response(data=res, status=status.HTTP_200_OK)


@api_view(["GET"])
def ListCuotas(request, ci):
    return Response({"ci": ci}, status=status.HTTP_200_OK)


@api_view(["POST"])
def PayExtraord(request, ci):
    user = UserAccount.objects.filter(username=ci).first()
    if not user:
        return Response(
            {"detail": "no se encontro ci"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = CuotaArraySerializer(data=request.data)

    if serializer.is_valid():
        cuotas = serializer.validated_data["cuotas"]
        resultados = Cuota.objects.filter(id__in=cuotas)
        serializer_cu = CuotaSerializer(resultados, many=True)
        serializer_us = UserSerializer(user)
        return Response(
            {"user": serializer_us.data, "cuotas": serializer_cu.data},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def GenerarCuotas(request, ci):
    serializer = CuotaInputSerializer(data=request.data)
    if serializer.is_valid():
        amount = serializer.validated_data["amount"]
        term = serializer.validated_data["term"]
        return Response({"ci": ci, "cuotas": {}}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
