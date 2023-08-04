from django.urls import include, path
from rest_framework import routers
from authapi import views

router = routers.DefaultRouter()
router.register("notificacion", views.NotificacionView)
router.register("token", views.TokenView)

urlpatterns = [
    path("/", include(router.urls)),
]
