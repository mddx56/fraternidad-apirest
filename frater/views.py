from rest_framework import viewsets
from .serializer import (
    CumpleanioSerializer,
    FraternidadSerializer,
)


from .models import (
    Fraternidad,
    Cumpleanio,
)


class FraternidadView(viewsets.ModelViewSet):
    serializer_class = FraternidadSerializer
    queryset = Fraternidad.objects.all()


class CumpleanioView(viewsets.ModelViewSet):
    serializer_class = CumpleanioSerializer
    queryset = Cumpleanio.objects.all()
