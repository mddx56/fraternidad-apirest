from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView
from core import views
from apps.accounts.views import (
    ChangePasswordView,
    ObtainTokenPairView,
    UpdateProfileView,
)
from apps.accounts.views import CreateUserView

schema_view = get_schema_view(
    openapi.Info(
        title="Frater",
        default_version="v1",
        description="Fraternidad Agenda",
        contact=openapi.Contact(email="mddx56@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="inicio"),
    path("privacy/", views.privacy, name="politicas"),
    path("home/", views.home, name="home.."),
    path("api/login", ObtainTokenPairView.as_view(), name="login_user"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/signup", CreateUserView.as_view(), name="create_user"),
    path(
        "api/change_password/<str:pk>/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "api/update_profile/<str:pk>/",
        UpdateProfileView.as_view(),
        name="update_profile",
    ),
    path("api/agenda/", include("apps.agendas.urls")),
    path("api/frater/", include("apps.config.urls")),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/notif/", include("apps.notifications.urls")),
]


if settings.DEBUG:
    urlpatterns = [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ] + urlpatterns
