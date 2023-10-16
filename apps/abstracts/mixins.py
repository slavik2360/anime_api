# Python
from typing import Any

# DRF
from rest_framework.exceptions import APIException



# Django
from django.db.models import query


class CustomValidationException(APIException):
    """Абстрактный вспомогательный класс для ошибок."""
    status_code = 400
    default_detail = 'что-то пошло не так!!!'
    default_code = 'твой кастомный валидатор на ошибку 400'

    def __init__(self, detail=default_detail, code=status_code):
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.code = code
