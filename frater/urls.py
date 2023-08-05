from django.urls import include, path
from rest_framework import routers
from frater import views

router = routers.DefaultRouter()
router.register("cumple", views.CumpleanioView)
router.register("fraternidad", views.FraternidadView)

urlpatterns = [
    path("/", include(router.urls)),
]
