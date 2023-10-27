# Python
from typing import Optional
# DRF
from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
=======
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response as JsonResponse
>>>>>>> 050cb8c (Permission)
from rest_framework.exceptions import ValidationError
from django.db.models.functions import Lower
from django.db.models import Q
# LOCAL
<<<<<<< HEAD
from .models import (
=======
from anime.models import (
>>>>>>> 050cb8c (Permission)
    Genre,
    Season,
    Episode,
    Anime,
    Comment
)
<<<<<<< HEAD
from abstracts.mixins import CustomValidationException
=======
from abstracts.mixins import ResponseMixin, ObjectMixin
from .permissions import AnimePermission
>>>>>>> 050cb8c (Permission)
from .serializers import(
   GenreSerializer,
   GenreCreateSerializer,
   AnimeSerializer,
   AnimeCreateSerializer,
   CommentSerializer,
   CommentCreateSerializer
)



<<<<<<< HEAD
class AnimeViewSet(viewsets.ViewSet,):
    """
    ViewSet for Anime model.
    """
=======
class AnimeViewSet(ViewSet, ResponseMixin, ObjectMixin):
    """
    ViewSet for Anime model.
    """
    permission_classes = (
        AnimePermission,
    )
>>>>>>> 050cb8c (Permission)
    queryset = Anime.objects.all()

    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
<<<<<<< HEAD
    )->Response:
            serializer = AnimeSerializer(
                instance=self.queryset, 
                many=True
            )
            return Response(
                data=serializer.data
            )
=======
    )->JsonResponse:
        serializer = AnimeSerializer(
            instance=self.queryset, 
            many=True
        )
        return self.json_response(
            data=serializer.data
        )
>>>>>>> 050cb8c (Permission)

    def retrieve(
        self,
        request:Request,
        pk: Optional[int] = None
<<<<<<< HEAD
    )->Response:
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            raise CustomValidationException(detail=f'Anime with such an {pk} does not exist', code=400)
        serializer = AnimeSerializer(anime)
        return Response(
            data=serializer.data
        )
=======
    )->JsonResponse:
        anime = self.get_object(self.queryset, pk)
        serializer = AnimeSerializer(anime)
        return self.json_response(serializer.data)
>>>>>>> 050cb8c (Permission)

    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
<<<<<<< HEAD
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
=======
    )->JsonResponse:
        serializer = AnimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return self.json_response(f'{anime.title} is created. ID: {anime.id}')
>>>>>>> 050cb8c (Permission)

    def update(
        self,
        request:Request,
<<<<<<< HEAD
        pk: Optional[int] = None,
        *args:tuple,
        **kwargs:dict
    )->Response:
        anime = get_object_or_404(Anime, pk=pk)
=======
        pk: Optional[int] = None
    )->JsonResponse:
        anime = self.get_object(self.queryset, pk)
>>>>>>> 050cb8c (Permission)
        serializer = AnimeCreateSerializer(
            instance=anime, 
            data=request.data
        )
<<<<<<< HEAD
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Anime {anime.title} is updated!'
            }
        )
=======
        if not serializer.is_valid():
            return self.json_response(
                f'{anime.title} wasn\'t updated', 'Warning'
            )
        anime: Anime = serializer.save()
        return self.json_response(f'{anime.title} was updated')
>>>>>>> 050cb8c (Permission)

    def partial_update(
        self,
        request:Request,
<<<<<<< HEAD
        pk: Optional[int] = None,
        *args:tuple,
        **kwargs:dict
    )->Response:
        anime = get_object_or_404(Anime, pk=pk)
=======
        pk: Optional[int] = None
    ) -> JsonResponse:
        anime = self.get_object(self.queryset, pk)
>>>>>>> 050cb8c (Permission)
        serializer = AnimeCreateSerializer(
            instance=anime, 
            data=request.data, 
            partial=True
        )
<<<<<<< HEAD
        serializer.is_valid(raise_exception=True)
        anime: Anime = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Anime {anime.title} is partial_update!'
            }
        )
=======
        if not serializer.is_valid():
            return self.json_response(
                f'{anime.title} wasn\'t partially-updated', 'Warning'
            )
        anime: Anime = serializer.save()
        return self.json_response(f'{anime.title} was partially-updated')
>>>>>>> 050cb8c (Permission)

    def destroy(
        self,
        request:Request,
        pk: Optional[int] = None,
        *args:tuple,
        **kwargs:dict
<<<<<<< HEAD
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
            raise CustomValidationException(detail=f'Anime with such an {pk} does not exist', code=400)
        

class AnimeSearchViewSet(viewsets.ViewSet):
=======
    )->JsonResponse:
        anime = self.get_object(self.queryset, pk)
        name = anime.title
        anime.delete()
        return self.json_response(f'{name} was deleted')
        
        

class AnimeSearchViewSet(ViewSet):
>>>>>>> 050cb8c (Permission)
    """
    ViewSet Search name Anime for Game model.
    """
    queryset = Anime.objects.all()
    
    def list(
        self,
        request: Request,
        *args:tuple,
        **kwargs:dict
<<<<<<< HEAD
    ) -> Response:
=======
    ) -> JsonResponse:
>>>>>>> 050cb8c (Permission)
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
        
<<<<<<< HEAD
        return Response(data=serializer.data)
=======
        return JsonResponse(data=serializer.data)
>>>>>>> 050cb8c (Permission)
