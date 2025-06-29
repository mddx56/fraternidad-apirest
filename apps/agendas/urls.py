from django.urls import include, path
from rest_framework import routers
from apps.agendas import views

router = routers.DefaultRouter()
router.register("tiposevent", views.TipoEventoView)
router.register("agendas", views.AgendaView)
router.register("pagoagendas", views.DetallePagoEventoView)
router.register("gestions", views.GestionView)
router.register("mensualidads", views.MensualidadView)
router.register("pagomensualidades", views.DetallePagoMensualidadView)
router.register("extraordinarias", views.ExtraordinariaView)
router.register("pagoextraordinarias", views.DetallePagoExtraordianriaView)
router.register("pagos", views.PagoView)
router.register("qrs", views.QrView)
router.register("grupoturnos", views.GrupoTurnoView)
router.register("turnos", views.TurnoView)
router.register("userturnos", views.UserTurnoView)
router.register("cupon", views.CuponView)

urlpatterns = [
    path("", include(router.urls)),
    path("pagos/m/<ci>", views.ListPagosView.as_view(), name="pagos"),
    path(
        "deudas/m/<str:ci>",
        views.ListMensualidadDeudaView,
        name="deudas_mensual",
    ),
    path(
        "deudas/mg/<str:ci>",
        views.ListMensualidadDeudaAllGestionsView,
        name="deudas_mensual_gestion_all",
    ),
    path("deudas/e/<ci>", views.ListDeudaExtraordinaria, name="deudas_extraordinaria"),
    path("grupo-view/<id>", views.ListFratersGroup, name="fraternos_por_grupo"),
    path("grupo-all/", views.ListGroups, name="fraternos_grupo"),
    path("generar-cuotas/<str:ci>/", views.GenerarCuotas, name="Generar cuotas"),
    path("cuotas-all/<str:ci>/", views.ListCuotas, name="Listar cuotas"),
    path("pagar-cuotas/<str:ci>/", views.PayExtraord, name="Pagar cuotas"),
    path("pagar-mensuals/", views.PayMensualidades, name="Pagar mensualidades"),
    path("reserva/", views.ReservaEvento, name="Reserva evento"),
    path("pagar-reserva/", views.PagoReservaEvento, name="Pago reserva"),
    path("reserva-especial/", views.EventoFraterno, name="Reserva solo fraternos"),
    path("cupon-list-user/<ci>", views.ListCuponesUserView.as_view(), name=""),
    path("cupon-estado/", views.CuponEstadoView, name=""),
    path("cupon-list/", views.ListCuponsValView, name=""),
]
