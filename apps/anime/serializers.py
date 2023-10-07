# DRF
from rest_framework import serializers

#local
from .models import (
    Genre,
    Anime,
    Season,
    Episode,
    Comment,
)
from auths.models import MyUser


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()


class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields = '__all__'


class EpisodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    episode_number = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    video = serializers.FileField()


class EpisodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Episode
        fields = '__all__'


class SeasonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    season_number = serializers.IntegerField()
    episodes = EpisodeSerializer(many=True)


class SeasonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Season
        fields = '__all__'

    
class AnimeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=300)
    rate = serializers.FloatField()
    poster = serializers.ImageField()
    genres = GenreSerializer(many=True)
    season = SeasonSerializer(many=True)


class AnimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Anime
        fields = '__all__'


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=MyUser.objects.all()
    )
    text = serializers.CharField(
        max_length=254
    )
    anime_id = serializers.PrimaryKeyRelatedField(
        queryset=Anime.objects.all()
    )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'

