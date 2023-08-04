from rest_framework import viewsets
from .serializers import (
    TokenSerializer,
    NotificacionSerializer,
)
from .models import Notificacion, Token


class TokenView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class NotificacionView(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()
