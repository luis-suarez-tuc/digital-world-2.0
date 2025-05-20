from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == status.HTTP_401_UNAUTHORIZED:
        response.data = {
            "message": "Por favor, inicia sesión para continuar.",
            "status_code": response.status_code
        }

    return response