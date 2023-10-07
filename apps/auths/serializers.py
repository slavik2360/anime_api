# DRF
from rest_framework import serializers
from django.core.validators import EmailValidator

#local
from auths.models import MyUser
from abstracts.utils import validate_mail


class MyUserSerializer(serializers.Serializer):
    """
    Cериалайзер пользователя.
    """
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    nickname = serializers.CharField(max_length=120)

    def validate_email(self, value: str):
        """
        Кастом валидация email.
        """
        if validate_mail(value) != "GOOD":
            raise serializers.ValidationError('Неверный формат адреса электронной почты.')
        return value
    
    def create(self, validated_data):
        self.is_valid(raise_exception=True)
        validated_data = self.validated_data
        validated_data['email'] = self.validate_email(validated_data['email'])
        my_user = MyUser.objects.create(**validated_data)
        return my_user