from django.urls import include, path
from rest_framework import routers
from configuracion import views

router = routers.DefaultRouter()
# router.register("notificacions", views.NotificacionView)
# router.register("tokens", views.TokenView)
router.register("cumples", views.CumpleanioView)
router.register("fraternidad", views.FraternidadView)
router.register("mediaimages", views.MediaImageView)
router.register("mediavideos", views.MediaVideoView)
router.register("articuloss", views.ArticuloView)


urlpatterns = [
    path("/", include(router.urls)),
]
