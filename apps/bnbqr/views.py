from django.http import HttpResponse
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QRGenerationSerializer
from .services import BNBApiService
from .models import QRRecord
from apps.accounts.services import JWTService


class GenerateQRCodeView(APIView):

    def post(self, request):
        # user = JWTService.get_user(request)

        format_type = request.query_params.get("format", "json").lower()

        serializer = QRGenerationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            qr_record = QRRecord(
                user_craeted=request.user,
                moneda=BNBApiService.DEFAULT_CURRENCY,
                monto=serializer.validated_data["amount"],
                concepto=serializer.validated_data["gloss"],
                unsolouso=serializer.validated_data["singleUse"],
                fecha_expiracion=serializer.validated_data["expirationDate"],
                datos=serializer.validated_data.get("additionalData", ""),
                cuenta_destino=serializer.validated_data["destinationAccountId"],
            )

            token = BNBApiService.get_bnb_token()
            qr_response = BNBApiService.generate_qr_code(
                token, serializer.validated_data
            )

            qr_record.qr_id = qr_response.get("id")
            qr_record.generado = qr_response.get("success", False)
            qr_record.api_message = qr_response.get("message", "")
            qr_record.save()

            if not qr_response.get("success"):
                return Response(
                    {
                        "success": False,
                        "message": qr_response.get("message", "Error al generar QR"),
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            if format_type == "image":
                qr_image_data = base64.b64decode(qr_response["qr"])
                response = HttpResponse(qr_image_data, content_type="image/png")
                response["Content-Disposition"] = 'inline; filename="qr.png"'
                return response
            else:
                return Response(qr_response)

        except Exception as e:
            if "qr_record" in locals():
                qr_record.success = False
                qr_record.api_message = str(e)
                qr_record.save()

            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
