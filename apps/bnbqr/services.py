import requests
from django.conf import settings
from requests.exceptions import RequestException


class BNBApiService:
    DEFAULT_CURRENCY = "BOB"

    @staticmethod
    def get_bnb_token():
        url = f"{settings.BNB_API_URL}/ClientAuthentication.API/api/v1/auth/token"
        payload = {
            "accountId": settings.BNB_ACCOUNT_ID,
            "authorizationId": settings.BNB_AUTHORIZATION_ID,
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

            if data.get("success"):
                return data.get("message")
            raise Exception(
                "Failed to get token: " + str(data.get("message", "Unknown error"))
            )

        except RequestException as e:
            raise Exception(f"Error connecting to BNB API: {str(e)}")

    @staticmethod
    def generate_qr_code(token, qr_data):
        url = f"{settings.BNB_API_URL}/QRSimple.API/api/v1/main/getQRWithImageAsync"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        payload = {
            "currency": BNBApiService.DEFAULT_CURRENCY,
            "gloss": str(qr_data["gloss"]),
            "amount": float(qr_data["amount"]),
            "singleUse": bool(qr_data["singleUse"]),
            "expirationDate": str(qr_data["expirationDate"]),
            "additionalData": str(qr_data.get("additionalData", "")),
            "destinationAccountId": str(qr_data["destinationAccountId"]),
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()

        except RequestException as e:
            raise Exception(f"Error generating QR code: {str(e)}")
