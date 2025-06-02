import jwt
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request


User = get_user_model()


class JWTService:

    @staticmethod
    def get_raw_token(request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split(" ")
            return token if prefix.lower() == "bearer" else None
        except ValueError:
            return None

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expirado")
        except jwt.DecodeError:
            raise AuthenticationFailed("Token inválido")
        except Exception as e:
            raise AuthenticationFailed(f"Error procesando token: {str(e)}")

    @staticmethod
    def prepare_claims_for_json(claims):
        if not claims:
            return None

        prepared_claims = {}
        for key, value in claims.items():
            if key == "user_id" and hasattr(value, "hex"):
                prepared_claims[key] = str(value)
            elif key in ["exp", "iat", "nbf"] and hasattr(value, "timestamp"):
                prepared_claims[key] = int(value.timestamp())
            else:
                prepared_claims[key] = value
        return prepared_claims

    @staticmethod
    def get_claims(request):
        token = JWTService.get_raw_token(request)
        if not token:
            return None

        claims = JWTService.decode_token(token)
        return JWTService.prepare_claims_for_json(claims)

    @staticmethod
    def get_user(request: Request):
        try:
            claims = JWTService.get_claims(request)
            if not claims or "user_id" not in claims:
                return None

            user_id = claims["user_id"]

            if not user_id:
                return None

            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None
        except Exception as e:
            return None
