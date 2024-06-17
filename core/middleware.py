from http import HTTPStatus
from django.http import JsonResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class JSONErrorMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response.charset = "utf-8"
        status_code = response.status_code
        reason_phrase = response.reason_phrase
        if status_code == HTTPStatus.NOT_FOUND:
            return JsonResponse(
                {
                    "detail": "El recurso solicitado no se encontró. ☠",
                    "code": reason_phrase,
                },
                status=status_code,
            )
        
        return response
