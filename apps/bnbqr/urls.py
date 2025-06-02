from django.urls import path
from .views import GenerateQRCodeView

urlpatterns = [
    path("generate-qr/", GenerateQRCodeView.as_view(), name="generate-qr"),
]
