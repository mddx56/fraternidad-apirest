from rest_framework import serializers
from decimal import Decimal


class QRGenerationSerializer(serializers.Serializer):
    # currency = serializers.CharField(default="BOB")
    gloss = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    singleUse = serializers.BooleanField(default=True)
    expirationDate = serializers.DateField()
    additionalData = serializers.CharField(required=False)
    destinationAccountId = serializers.CharField()

    def validate_amount(self, value):
        """Asegura que el amount sea positivo y lo convierte a float."""
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor que cero.")
        return float(value)
