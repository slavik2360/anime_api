from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import (
    Genre,
    Anime,
    VideoFileType,
    Comment,
)
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import(
   GenreSerializer,
   GenreCreateSerializer,
   AnimeSerializer,
   AnimeCreateSerializer,
   VideoTupeSerializer,
   VideoTupeCreateSerializer,
   CommentSerializer,
   CommentCreateSerializer
)
from rest_framework.exceptions import ValidationError


from .models import Anime
from .serializers import AnimeSerializer, AnimeCreateSerializer



class AnimeViewSet(viewsets.ViewSet):
    queryset = Anime.objects.all()

    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = AnimeSerializer(
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
            anime = get_object_or_404(self.queryset, pk=pk)
        except Anime.DoesNotExist:
            raise ValidationError('Anime with such an ID does not exist',code=404)
        serializer = AnimeSerializer(anime)
        return Response(
            data=serializer.data
        )

    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = AnimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Anime {anime.title} is created!'
            }
        )

    def update(
        self,
        request:Request,
        pk = None,
        *args:tuple,
        **kwargs:dict
    )->Response:
        anime = get_object_or_404(Anime, pk=pk)
        serializer = AnimeCreateSerializer(
            instance=anime, 
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Anime {anime.title} is updated!'
            }
        )

    def partial_update(
        self,
        request:Request,
        pk = None,
        *args:tuple,
        **kwargs:dict
    )->Response:
        anime = get_object_or_404(Anime, pk=pk)
        serializer = AnimeCreateSerializer(
            instance=anime, 
            data=request.data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Anime {anime.title} is partial_update!'
            }
        )

    def destroy(
        self,
        request:Request,
        pk = None,
        *args:tuple,
        **kwargs:dict
    )->Response:
        try:
            anime = get_object_or_404(Anime, pk=pk)
            anime.delete()
            return Response(
                data={
                    'status':'ok',
                    'message':f'Anime {anime.title} is partial_update!'
                }
            )
        except anime.DoesNotExist:
            raise ValidationError('Anime with such an ID does not exist',code=404)
