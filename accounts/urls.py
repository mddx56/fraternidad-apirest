from django.urls import include, path
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register("notificacions", views.NotificacionView)
router.register("tokens", views.TokenView)
router.register("cumples", views.CumpleanioView)

urlpatterns = [    
    path("/", include(router.urls)),
]
