from django.db import transaction
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Sum
from datetime import datetime, date, timedelta
import calendar
from apps.accounts.models import UserAccount
from apps.accounts.serializers import UserSerializer
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
    Cuota,
    Cupon,
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
    MensualidadPaySerializer,
    ReservaPaySerializer,
    AgendaFraternoSerializer,
    CuponSerializer,
    CuponEstadoSerializer,
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


class CuponView(viewsets.ModelViewSet):
    serializer_class = CuponSerializer
    queryset = Cupon.objects.all()


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
    fecha_actual = datetime.now()
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
        user = UserAccount.objects.filter(username=ci).first()

        if user is None:
            return Response(
                {"detail": f"fraterno {ci} no encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        anio = datetime.today().year
        gestion = Gestion.objects.filter(anio=anio, en_curso=True).first()

        if not gestion:
            return Response(
                {"detail": "no existe gestion actual en curso"},
                status=status.HTTP_404_NOT_FOUND,
            )
        deudas = []
        mensualidades = Mensualidad.objects.filter(gestion=gestion).order_by("mes")
        detalle = DetallePagoMensualidad.objects.filter(
            pago__user=user, mensualidad__gestion__anio=anio
        )
        detalle_ini = detalle.order_by("mensualidad__fecha").last()
        for mensu in mensualidades:
            mes = mensu.mes
            if mes > detalle_ini.mensualidad.mes and is_valido_date(mes, anio):
                deudas.append(
                    {
                        "id": mensu.id,
                        "mes": dato_to_moth(mensu.mes),
                        "gestion": anio,
                        "costo": mensu.costo,
                        "fecha": mensu.fecha,
                        "mensualidad": mensu.pk,
                    }
                )

        suma = sum([num["costo"] for num in deudas])

        return Response({"deudas": deudas, "total": suma}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def ListMensualidadDeudaGestionView(request, ci):
    try:
        user = UserAccount.objects.filter(username=ci).first()

        if user is None:
            return Response(
                {"detail": f"fraterno {ci} no encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        anio = datetime.today().year
        gestion = Gestion.objects.filter(anio=anio, en_curso=True).first()

        if not gestion:
            return Response(
                {"detail": "no existe gestion actual en curso"},
                status=status.HTTP_404_NOT_FOUND,
            )
        deudas = []
        mensualidades = Mensualidad.objects.filter(gestion=gestion).order_by("mes")
        detalle = DetallePagoMensualidad.objects.filter(
            pago__user=user, mensualidad__gestion__anio=anio
        )
        detalle_ini = detalle.order_by("mensualidad__fecha").last()
        for mensu in mensualidades:
            mes = mensu.mes
            if mes > detalle_ini.mensualidad.mes:
                deudas.append(
                    {
                        "id": mensu.id,
                        "mes": dato_to_moth(mensu.mes),
                        "gestion": anio,
                        "costo": mensu.costo,
                        "fecha": mensu.fecha,
                        "mensualidad": mensu.pk,
                    }
                )

        gestiones = Gestion.objects.order_by("anio")

        for g in gestiones:
            mensualidades = Mensualidad.objects.filter(gestion=g).order_by("mes")
            if g.anio > anio:
                for me in mensualidades:
                    deudas.append(
                        {
                            "id": me.id,
                            "mes": dato_to_moth(me.mes),
                            "gestion": g.anio,
                            "costo": me.costo,
                            "fecha": me.fecha,
                            "mensualidad": me.pk,
                        }
                    )

        suma = sum([num["costo"] for num in deudas])

        return Response({"deudas": deudas, "total": suma}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def ListMensualidadDeudaAllGestionsView(request, ci):
    user = UserAccount.objects.filter(username=ci).first()

    if user is None:
        return Response(
            {"detail": f"fraterno {ci} no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )

    # anio = datetime.today().year
    gestiones = Gestion.objects.order_by("anio")
    gestion = Gestion.objects.order_by("anio").first()

    if not gestiones:
        return Response(
            {"detail": "no existe gestion actual en curso"},
            status=status.HTTP_404_NOT_FOUND,
        )
    deudas = []

    mensualidades = Mensualidad.objects.filter(gestion=gestion).order_by("mes")
    detalle = DetallePagoMensualidad.objects.filter(
        pago__user=user, mensualidad__gestion__anio=gestion.anio
    )

    detalle_ini = detalle.order_by("mensualidad__fecha").last()

    for mensu in mensualidades:
        mes = mensu.mes
        if mes > detalle_ini.mensualidad.mes:
            deudas.append(
                {
                    "id": mensu.id,
                    "mes": dato_to_moth(mensu.mes),
                    "gestion": gestion.anio,
                    "costo": mensu.costo,
                    "fecha": mensu.fecha,
                    "mensualidad": mensu.pk,
                }
            )

    gestion2 = Gestion.objects.order_by("anio").last()

    mensualidades = Mensualidad.objects.filter(gestion=gestion2).order_by("mes")
    for me in mensualidades:
        mes = me.mes
        if is_valido_date(mes, gestion2.anio):
            deudas.append(
                {
                    "id": me.id,
                    "mes": dato_to_moth(me.mes),
                    "gestion": gestion2.anio,
                    "costo": me.costo,
                    "fecha": me.fecha,
                    "mensualidad": me.pk,
                }
            )

    suma = sum([num["costo"] for num in deudas])

    return Response({"deudas": deudas, "total": suma}, status=status.HTTP_200_OK)


@api_view(["GET"])
def ListDeudaExtraordinaria(request, ci):
    frater = UserAccount.objects.get(username=ci)
    extraordinarias = Extraordinaria.objects.all()

    deudax = []

    sum = 0

    for extra in extraordinarias:
        sum = 0
        detalles = DetallePagoExtraordianria.objects.filter(
            pago__user=frater, extraordinaria=extra
        )
        total_extra = extra.monto
        extra = extra.to_json()
        for detalle in detalles:
            sum = sum + detalle.pago.monto_pagado
        deuda = total_extra - sum
        deudax.append({"extraordinaria": extra, "saldo": deuda, "deuda": total_extra})

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


from django.db import transaction


@api_view(["POST"])
def PayMensualidades(request):
    serializer = MensualidadPaySerializer(data=request.data)

    if serializer.is_valid():
        frater_id = serializer.validated_data["frater_id"]
        mensualidades = serializer.validated_data["mensualidades"]
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        with transaction.atomic():
            sum_total = Mensualidad.objects.filter(id__in=mensualidades).aggregate(
                total=Sum("costo")
            )
            total = sum_total["total"]

            pago = Pago.objects.create(
                fecha_pago=datetime.now().date(),
                monto_pagado=total,
                user_id=frater_id,
            )
            for ms_id in mensualidades:
                mns = Mensualidad.objects.get(id=ms_id)
                detalle = DetallePagoMensualidad.objects.create(
                    mensualidad=mns, pago=pago
                )
            serializer_pago = PagoSerializer(pago)
            return Response(
                {
                    "status": "success",
                    "pago": serializer_pago.data,
                    "cantidad": len(mensualidades),
                    "total": total,
                },
                status=status.HTTP_200_OK,
            )
    except Exception as e:
        return Response(
            {"error": f"Error al crear pagos: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def es_finsemana(fecha):
    day = fecha.weekday()
    if day >= 5:
        return True
    return False


def validate_fecha(fecha):
    hoy = datetime.now().date()
    if fecha <= hoy:
        return False
    return True


@api_view(["POST"])
def ReservaEvento(request):
    try:
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            date_reserva = serializer.validated_data["fecha"]
            if not validate_fecha(date_reserva):
                return Response(
                    data={"detail": "La fecha debe ser mayor al día de hoy."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            dates = Agenda.objects.filter(fecha=date_reserva)
            if dates.exists():
                return Response(
                    data={"detail": "La fecha ya está reservada."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            reserva = Agenda.objects.create(**serializer.validated_data)
            reserva.es_entresemana = not es_finsemana(date_reserva)
            reserva.save()
            reserva_serializer = AgendaSerializer(reserva)
            return Response(
                data=reserva_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"detail": f"Error al crear reserva: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def get_month_start_end(now_date: date):
    start_day = now_date.replace(day=1)
    last_day = calendar.monthrange(now_date.year, now_date.month)[1]
    end_day = now_date.replace(day=last_day)
    return start_day, end_day


@api_view(["POST"])
def ReservaEventoFraterno(request):
    try:
        serializer = AgendaFraternoSerializer(data=request.data)
        if serializer.is_valid():
            date_reserva = serializer.validated_data["fecha"]
            data_user = serializer.validated_data["user"]
            data_user_id = serializer.data["user"]

            if not validate_fecha(date_reserva):
                return Response(
                    data={"detail": "La fecha debe ser mayor al día de hoy."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            inicio, fin = get_month_start_end(date_reserva)
            eventos = Agenda.objects.filter(fecha__range=(inicio, fin))
            evts = eventos.filter(user__id=data_user_id).filter(tipo_evento=None)
            if evts.count() > 0:
                return Response(
                    data={
                        "detail": f"{data_user} ya realizo una reserva solo para fraternos durante este mes."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            dates = Agenda.objects.filter(fecha=date_reserva).filter(tipo_evento=None)
            if dates.exists():
                return Response(
                    data={"detail": "La fecha ya está reservada."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            reserva = Agenda.objects.create(**serializer.validated_data)
            reserva.es_entresemana = not es_finsemana(date_reserva)
            reserva.save()
            reserva_serializer = AgendaSerializer(reserva)
            return Response(
                data=reserva_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"detail": f"Error al crear reserva: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


from apps.shared.constants import EVENT_FREE


@api_view(["POST"])
def EventoFraterno(request):
    try:
        serializer = AgendaFraternoSerializer(data=request.data)
        if serializer.is_valid():
            date_reserva = serializer.validated_data["fecha"]
            data_user = serializer.validated_data["user"]
            data_user_id = serializer.data["user"]

            if not validate_fecha(date_reserva):
                return Response(
                    data={"detail": "La fecha debe ser mayor al día de hoy."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            print(EVENT_FREE)
            event_frater = TipoEvento.objects.filter(nombre=EVENT_FREE).first()
            if event_frater is None:
                event_frater = TipoEvento.objects.create(nombre=EVENT_FREE)

            inicio, fin = get_month_start_end(date_reserva)
            eventos = Agenda.objects.filter(fecha__range=(inicio, fin))
            evts = eventos.filter(user__id=data_user_id).filter(
                tipo_evento=event_frater
            )

            if evts.count() > 0:
                return Response(
                    data={
                        "detail": f"{data_user} ya realizo una reserva solo para fraternos durante este mes."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            dates = Agenda.objects.filter(fecha=date_reserva).filter(
                tipo_evento=event_frater
            )
            if dates.exists():
                return Response(
                    data={"detail": f"La fecha ya está reservada {EVENT_FREE}."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(data={"detail": "OK"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"detail": f"Error reserva especial: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def PagoReservaEvento(request):
    serializer = ReservaPaySerializer(data=request.data)
    if serializer.is_valid():
        frater_id = serializer.validated_data["frater_id"]
        evento_id = serializer.validated_data["evento"]
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        with transaction.atomic():
            evento = Agenda.objects.get(id=evento_id)
            if evento is None:
                return Response(
                    {"detail": "El evento no existe."}, status=status.HTTP_404_NOT_FOUND
                )
            detalle = DetallePagoEvento.objects.get(evento__id=evento_id)
            if detalle is not None:
                return Response(
                    {"detail": "El evento ya fue pagado."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if evento is None:
                return Response(
                    {"detail": "El evento no existe."}, status=status.HTTP_404_NOT_FOUND
                )
            evento.estado_reserva = Agenda.ACTIVA
            evento.save()
            tipo_evento = TipoEvento.objects.get(id=evento.tipo_evento.id)
            precio = (
                tipo_evento.costo_entresemana
                if evento.es_entresemana
                else tipo_evento.costo_finsemana
            )
            pago = Pago.objects.create(
                fecha_pago=datetime.now().date(),
                monto_pagado=precio,
                user_id=frater_id,
            )
            detalle = DetallePagoEvento.objects.create(pago=pago, evento=evento)
            serializer_pago = PagoSerializer(pago)
            return Response(
                {
                    "status": "success",
                    "pago": serializer_pago.data,
                    "cantidad": 1,
                    "total": precio,
                },
                status=status.HTTP_200_OK,
            )
    except Exception as e:
        return Response(
            {"detail": f"Error al crear reserva: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class ListCuponesUserView(APIView):
    def get(self, request, ci, format=None):
        try:
            frater = UserAccount.objects.filter(username=ci).first()
            if frater:
                cupones = Cupon.objects.filter(user=frater).filter(estado=True)
                serializer = CuponSerializer(cupones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def CuponEstadoView(request):
    serializer = CuponEstadoSerializer(data=request.data)
    try:
        if serializer.is_valid():
            cupon = serializer.validated_data["cupon"]
            estado = serializer.validated_data["estado"]

            cupon_data = Cupon.objects.get(pk=cupon)
            if cupon_data is None:
                return Response(
                    {"detail": "El cupon no existe."}, status=status.HTTP_404_NOT_FOUND
                )
            cupon_data.estado = estado
            cupon_data.save()
            return Response(
                {"status": "success", "cupon": " Estado de cupon actualizado.."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"detail": f"Error estado cupon: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def ListCuponsValView(request):
    try:
        cupons = Cupon.objects.filter(estado=True)
        serializer = CuponSerializer(cupons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)
