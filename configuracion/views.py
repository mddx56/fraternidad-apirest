from rest_framework import viewsets
from .models import Fraternidad, Medio
from .serializers import FraternidadSerializer, MedioSerializer


class FraternidadView(viewsets.ModelViewSet):
    serializer_class = FraternidadSerializer
    queryset = Fraternidad.objects.all()


class MedioView(viewsets.ModelViewSet):
    serializer_class = MedioSerializer
    queryset = Medio.objects.all()
