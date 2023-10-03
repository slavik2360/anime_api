# DRF
from rest_framework import serializers

#local
from auths.models import MyUser


class MyUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    nickname = serializers.CharField()
    is_staff = serializers.BooleanField()


class MyUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= MyUser
        fields = [
            'email',
            'nickname',
            'is_staff'
        ]