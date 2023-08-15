from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import TokenSerializer, NotificacionSerializer, UserSerializer
from .models import Notificacion, Token


class TokenView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class NotificacionView(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
