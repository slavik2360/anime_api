# Python
from typing import Any

# DRF
from rest_framework.exceptions import APIException

from rest_framework.response import Response as JsonResponse
from rest_framework.validators import ValidationError
from rest_framework.exceptions import APIException

# Django
from django.db.models import query




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

    def format_detail(self, *args, **kwargs):
        return self.detail.format(*args, **kwargs)


class ResponseMixin:
    """Абстрактный вспомогательный класс для респонсов."""

    STATUS_SUCCESS: str = 'Success'
    STATUS_WARNING: str = 'Warning'
    STATUS_ERROR: str = 'Error'
    STATUSES: tuple[str, ...] = (
        STATUS_SUCCESS,
        STATUS_WARNING,
        STATUS_ERROR
    )

    def json_response(
        self,
        data: Any,
        status: str = STATUS_SUCCESS
    ) -> JsonResponse:

        if status not in self.STATUSES:
            raise ValidationError('FATAL ERROR')

        return JsonResponse(
            {
                'status': status,
                'results': data
            }
        )
    
class ObjectMixin:
    """Абстрактный вспомогательный класс для объектов."""

    def get_object(
        self,
        queryset: query.QuerySet,
        obj_id: str
    ) -> Any:
        """Метод для вытаскивания объекта."""

        obj: Any = queryset.filter(id=obj_id).first()
        if obj is None:
            raise ValidationError(
                {
                    'status': 'Error',
                    'results': f'Object {obj_id} not found'
                }
            )
        return obj

