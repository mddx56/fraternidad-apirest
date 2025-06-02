from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from .serializers import (
    ChangePasswordSerializer,
    MyTokenObtainPairSerializer,
    UpdateUserSerializer,
    UserSerializer,
    UserFraterSerializer,
    UuIdSerializer,
)
from rest_framework.decorators import api_view
import rest_framework.status as status
from django.db.models import Q


User = get_user_model()
fraternos = Q(role="Fraterno") | Q(role="Tesorero")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(APIView):
    permission_classes(
        AllowAny,
    )

    def post(self, request):
        try:
            user = request.data
            print(user)
            serializer = UserSerializer(data=user)
        except (TypeError, ValueError, OverflowError):
            user = None
            serializer = None

        if user and serializer.is_valid(raise_exception=True):
            serializer.save()
            # user_obj = User.objects.get_by_natural_key(serializer.data["username"])
            return Response(
                {"message": "Agregado correctamente."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserDetailsView(APIView):
    permission_classes(
        AllowAny,
    )

    def get(self, request, id, *args, **kwargs):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user).data
        user_data = serializer

        return Response(user_data, status=status.HTTP_200_OK)


class ObtainTokenPairView(TokenObtainPairView):
    """permission_classes(
        AllowAny,
    )"""

    permission_classes = [AllowAny]

    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class CheckStatus(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        token = request.auth
        claims = token.payload if token else {}

        print(user.role)

        return Response(
            {
                "token": "valid",
                "claims": {
                    "token_type": claims.get("token_type"),
                    "exp": claims.get("exp"),
                    "iat": claims.get("iat"),
                    "jti": claims.get("jti"),
                },
                "id": user.id,
                "username": user.username,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role,
                "phone": user.phone,
                "suspend": user.suspend,
            },
            status=status.HTTP_200_OK,
        )


class ListFraternosActivos(generics.ListAPIView):
    queryset = User.objects.filter(fraternos).filter(suspend=True)
    serializer_class = UserFraterSerializer


class ListFraternos(generics.ListAPIView):
    queryset = User.objects.filter(fraternos)
    serializer_class = UserFraterSerializer


class ListFraternosInActivos(generics.ListAPIView):
    queryset = User.objects.filter(fraternos).filter(suspend=False)
    serializer_class = UserFraterSerializer


@api_view(["GET"])
def SuspendFraterno(request, id):
    user = request.user
    role = user.role
    serializer = UuIdSerializer(data={"id": id})

    if not serializer.is_valid():
        return Response(
            {"detail": "Uuid no valido o vacio"}, status=status.HTTP_400_BAD_REQUEST
        )

    update_user = get_object_or_404(User, pk=id)

    if role == "Admin" or role == "Tesorero":
        sw = not update_user.suspend
        update_user.suspend = sw
        update_user.save()
        return Response(
            {"detail": "estado de supend cambiado"},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"detail": "no autorizado"}, status=status.HTTP_401_UNAUTHORIZED
        )


def calcular_porcentaje(activos, total):
    if total == 0:
        return 0
    return (activos / total) * 100


@api_view(["GET"])
def CountFraternos(request):
    try:
        total = User.objects.filter(fraternos).count()
        activos = User.objects.filter(fraternos).filter(suspend=False).count()
        suspendidos = User.objects.filter(fraternos).filter(suspend=True).count()

        activos_porcent = calcular_porcentaje(activos, total)
        suspendidos_porcent = calcular_porcentaje(suspendidos, total)

        return Response(
            [
                {
                    "title": "Total Fraternos",
                    "value": total,
                    "icon": "total",
                    "description": "100%",
                },
                {
                    "title": "Activos",
                    "value": activos,
                    "icon": "act",
                    "description": f"↗︎{activos_porcent:.2f}%",
                },
                {
                    "title": "Suspendidos",
                    "value": suspendidos,
                    "icon": "sus",
                    "description": f"↙{suspendidos_porcent:.2f}%",
                },
            ],
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)
