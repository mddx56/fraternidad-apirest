from django.urls import include, path
from rest_framework import routers
from apps.accounts import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("fraternos/", views.ListFraternos.as_view()),
    path("fraternos-activos/", views.ListFraternosActivos.as_view()),
    path("fraternos-inactivos/", views.ListFraternosInActivos.as_view()),
    path("check-status/", views.CheckStatus.as_view()),
    path("fraternos-count/", views.CountFraternos),
    path("suspend/<str:id>/", views.SuspendFraterno),
]
