# DRF
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models.functions import Lower
from django.db.models import Q
# LOCAL
from .models import (
    Genre,
    Season,
    Episode,
    Anime,
    Comment
)
from .serializers import(
   GenreSerializer,
   GenreCreateSerializer,
   AnimeSerializer,
   AnimeCreateSerializer,
   CommentSerializer,
   CommentCreateSerializer
)



class AnimeViewSet(viewsets.ViewSet):
    """
    ViewSet for Anime model.
    """
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
        

class AnimeSearchViewSet(viewsets.ViewSet):
    """
    ViewSet Search name Anime for Game model.
    """
    queryset = Anime.objects.all()
    
    def list(
        self,
        request: Request,
        *args:tuple,
        **kwargs:dict
    ) -> Response:
        srch = request.query_params.get('srch', None)
        rate = request.query_params.get('rate', None)

        if srch is not None:
            self.queryset = self.queryset.filter(Q(title__iexact=srch) | Q(title__icontains=srch))

        if rate is not None:
            if 'min' in rate:
                self.queryset = self.queryset.order_by('-rate')
            else:
                self.queryset = self.queryset.order_by('rate')

        serializer: AnimeSerializer = \
            AnimeSerializer(
                instance=self.queryset,
                many=True
            )
        
        return Response(data=serializer.data)