from rest_framework import viewsets
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import (
    TokenSerializer,
    NotificacionSerializer,
    UserSerializer,
    CumpleanioSerializer,
)
from .models import Notificacion, Token, Cumpleanio, User




class CumpleanioView(viewsets.ModelViewSet):
    serializer_class = CumpleanioSerializer
    queryset = Cumpleanio.objects.all()


class TokenView(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class NotificacionView(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    queryset = Notificacion.objects.all()


class CreateUserView(APIView):
    permission_classes(
        AllowAny,
    )

    def post(self, request):
        try:
            user = request.data
            serializer = UserSerializer(data=user)
        except (TypeError, ValueError, OverflowError):
            user = None
            serializer = None

        if user and serializer.is_valid(raise_exception=True):
            serializer.save()
            user_obj = User.objects.get_by_natural_key(serializer.data["username"])
            return Response(
                {"message": "Agregado correctamente."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
