from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from .serializers import (
    ChangePasswordSerializer,
    MyTokenObtainPairSerializer,
    UpdateUserSerializer,
    UserSerializer,
)
import rest_framework.status as status


User = get_user_model()


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
    permission_classes(
        AllowAny,
    )

    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
