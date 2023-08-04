from django.urls import include, path
from rest_framework import routers
from frater import views

router = routers.DefaultRouter()
router.register("cumple", views.CumpleanioSerializerView)
router.register("fraternidad", views.FraternidadView)

urlpatterns = [
    path("/", include(router.urls)),
]
