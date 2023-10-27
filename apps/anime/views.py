# Python
from typing import Optional
# DRF
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response as JsonResponse
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
from abstracts.mixins import ResponseMixin, ObjectMixin
from .permissions import AnimePermission
from .serializers import(
   GenreSerializer,
   GenreCreateSerializer,
   AnimeSerializer,
   AnimeCreateSerializer,
   CommentSerializer,
   CommentCreateSerializer
)



class AnimeViewSet(ViewSet, ResponseMixin, ObjectMixin):
    """
    ViewSet for Anime model.
    """
    permission_classes = (
        AnimePermission,
    )
    queryset = Anime.objects.all()

    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->JsonResponse:
        serializer = AnimeSerializer(
            instance=self.queryset, 
            many=True
        )
        return self.json_response(
            data=serializer.data
        )

    def retrieve(
        self,
        request:Request,
        pk: Optional[int] = None
    )->JsonResponse:
        anime = self.get_object(self.queryset, pk)
        serializer = AnimeSerializer(anime)
        return self.json_response(serializer.data)

    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->JsonResponse:
        serializer = AnimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return self.json_response(f'{anime.title} is created. ID: {anime.id}')

    def update(
        self,
        request:Request,
        pk: Optional[int] = None
    )->JsonResponse:
        anime = self.get_object(self.queryset, pk)
        serializer = AnimeCreateSerializer(
            instance=anime, 
            data=request.data
        )
        if not serializer.is_valid():
            return self.json_response(
                f'{anime.title} wasn\'t updated', 'Warning'
            )
        anime: Anime = serializer.save()
        return self.json_response(f'{anime.title} was updated')

    def partial_update(
        self,
        request:Request,
        pk: Optional[int] = None
    ) -> JsonResponse:
        anime = self.get_object(self.queryset, pk)
        serializer = AnimeCreateSerializer(
            instance=anime, 
            data=request.data, 
            partial=True
        )
        if not serializer.is_valid():
            return self.json_response(
                f'{anime.title} wasn\'t partially-updated', 'Warning'
            )
        anime: Anime = serializer.save()
        return self.json_response(f'{anime.title} was partially-updated')

    def destroy(
        self,
        request:Request,
        pk: Optional[int] = None,
        *args:tuple,
        **kwargs:dict
    )->JsonResponse:
        anime = self.get_object(self.queryset, pk)
        name = anime.title
        anime.delete()
        return self.json_response(f'{name} was deleted')
        
        

class AnimeSearchViewSet(ViewSet):
    """
    ViewSet Search name Anime for Game model.
    """
    queryset = Anime.objects.all()
    
    def list(
        self,
        request: Request,
        *args:tuple,
        **kwargs:dict
    ) -> JsonResponse:
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
        
        return JsonResponse(data=serializer.data)