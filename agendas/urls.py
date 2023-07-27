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
router.register("detallesdeuda", views.DetalleDeudaView)
router.register("pagos", views.PagoView)
router.register("qrs", views.QrView)

urlpatterns = [
    path("/", include(router.urls)),
]