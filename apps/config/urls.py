from django.urls import include, path
from rest_framework import routers
from apps.config import views

router = routers.DefaultRouter()
# router.register("notificacions", views.NotificacionView)
# router.register("tokens", views.TokenView)
router.register("cumples", views.CumpleanioView)
router.register("fraternidad", views.FraternidadView)
router.register("mediaimages", views.MediaImageView)
router.register("mediavideos", views.MediaVideoView)
router.register("articulos", views.ArticuloView)

router.register("horarios", views.HorarioView)
router.register("diasemanas", views.DiaSemanaView)
router.register("cronogramas", views.CronogramaView)
router.register("actividades", views.ActividadView)


urlpatterns = [
    path("", include(router.urls)),
]
