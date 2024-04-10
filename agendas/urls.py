from django.urls import include, path
from rest_framework import routers
from agendas import views

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

urlpatterns = [
    path("/", include(router.urls)),
    path("/pagos/m/<ci>", views.ListPagosView.as_view(), name="pagos"),
    path("/deudas/m/<ci>", views.ListMensualidadDeudaView, name="deudas_mensualidad"),
    path("/deudas/e/<ci>", views.ListDeudaExtraordinaria, name="deudas_extraordinaria"),
]
