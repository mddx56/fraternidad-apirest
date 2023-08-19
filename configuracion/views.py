from rest_framework import viewsets
from .models import Cumpleanio, Token, Notificacion, Fraternidad, Medio
from .serializers import (
    CumpleanioSerializer,
    FraternidadSerializer,
    MedioSerializer,
    NotificacionSerializer,
    TokenSerializer,
)


class CumpleanioView(viewsets.ModelViewSet):
    serializer_class = CumpleanioSerializer
    queryset = Cumpleanio.objects.all()


class TokenView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class NotificacionView(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()


class FraternidadView(viewsets.ModelViewSet):
    serializer_class = FraternidadSerializer
    queryset = Fraternidad.objects.all()


class MedioView(viewsets.ModelViewSet):
    serializer_class = MedioSerializer
    queryset = Medio.objects.all()
