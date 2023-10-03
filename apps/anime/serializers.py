# DRF
from rest_framework import serializers

#local
from .models import (
    Genre,
    Anime,
    VideoFileType,
    Comment,
)

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields = [
            'name'
        ]
    

class AnimeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    rate = serializers.FloatField()
    poster = serializers.ImageField()
    video = serializers.FileField()
    genres = serializers.IntegerField()


class AnimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Anime
        fields = [
            'title',
            'description',
            'rate',
            'poster',
            'video',
            'genres'
        ]

class VideoTupeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class VideoTupeCreateSerializer(serializers.Serializer):
    class Meta:
        model= VideoFileType
        fields = [
            'name'
        ]

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    text = serializers.CharField()
    anime = serializers.IntegerField()


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = [
            'user',
            'text',
            'anime'
        ]