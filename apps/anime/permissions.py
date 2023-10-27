# DRF
from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class AnimePermission(BasePermission):

    def __init__(self) -> None:
        self.user_permission: bool = False
        self.admin_permission: bool = False

    def has_permission(
        self,
        request: Request,
        view: 'AnimeViewSet'
    ) -> bool:
        self.user_permission = (
            request.user and
            request.user.is_active
        )
        self.admin_permission = self.user_permission and (
            request.user.is_staff and
            request.user.is_superuser
        )
        if view.action in (
            'destroy',
        ):
            return self.admin_permission

        return self.user_permission