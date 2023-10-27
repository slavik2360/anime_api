# DRF
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
<<<<<<< HEAD
from rest_framework.permissions import (
    IsAuthenticated,
    BasePermission
)
=======
>>>>>>> 050cb8c (Permission)

#LOCAL
from auths.models import MyUser
from auths.serializers import MyUserSerializer


class MyUserViewSet(viewsets.ViewSet):
    """
    ViewSet for MyUser model.
    """
    queryset = MyUser.objects.all()
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]
=======
>>>>>>> 050cb8c (Permission)

    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = MyUserSerializer(
            instance=self.queryset, 
            many=True
        )
        return Response(
            data=serializer.data
        )

    def retrieve(
        self,
        request:Request,
        pk = None,
        *args:tuple,
        **kwargs:dict
    )->Response:
        try:
            user = get_object_or_404(self.queryset, pk=pk)
        except MyUser.DoesNotExist:
            raise ValidationError('USER with such an ID does not exist', code=404)
        serializer = MyUserSerializer(user)
        return Response(
            data=serializer.data
        )

    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        try:
            serializer = MyUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user: MyUser = serializer.save()
            return Response(
                data={
                    'status':'ok',
                    'message':f'user {user.nickname} is created!'
                }
            )
        except IntegrityError:
            raise ValidationError('This email already exists!', code=404)