from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from agendas import views

router = routers.DefaultRouter()
router.register("estadosreserva", views.EstadoReservaView)
router.register("tiposevent", views.TipoEventoSerializerView)
router.register("estadosdeuda", views.EstadoDeudaView)
router.register("agendas", views.AgendaView)
router.register("deudas", views.DeudaView)
#router.register("detallesdeuda", views.DetalleDeudaView)
router.register("pagos", views.PagoView)
router.register("qrs", views.QrView)
router.register("turnos", views.TurnoView)
router.register("userturnos", views.UserTurnoView)
router.register("mensualidads", views.MensualidadView)
router.register("extraordinarias", views.ExtraordinariaView)
router.register("deudaextraordinarias", views.DeudaExtraordinariaView)

urlpatterns = [
    path("/", include(router.urls)),
    path('fraterno/<str:id>/deudas/', views.DeudasPorClienteListView.as_view(), name='eventos-all'),
]