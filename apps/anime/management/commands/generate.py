import requests
import random
import datetime
from typing import Any, Optional
from django.core.management import BaseCommand
from django.db.models.query import QuerySet
from django.db.utils import IntegrityError

from anime.models import (
    Genre,
    Anime
)
from AnilistPython import Anilist
from string import ascii_letters


class Command(BaseCommand):
    """Command for generate data for Database."""

    def create_genres(self) -> None:
        _genres_pattern: set[str] = {
               'Кодомо',
                'Сёдзё',
                'Дзёсэй',
                'Сёнэн',
                'Сэйнэн',
                'Апокалиптика',
                'Безумие',
                'Биопанк',
                'Боевик',
                'Боевые искусства',
                'Вампиры',
                'Военны',
                'Гарем',
                'Демоны',
                'Детектив',
                'Добуцу',
                'Драма',
                'Игры',
                'Идолы',
                'Икудзи',
                'Исэкай',
                'Исторический',
                'Кайто',
                'Киберпанк',
                'Комедия',
                'Космическая оперa',
                'Космос',
                'Магия',
                'Махо-сёдзё',
                'Машины',
                'Меха',
                'Мистика',
                'Моэ',
                'Музыка',
                'Мыльная опера',
                'Отаку',
                'Парапсихология',
                'Пародия',
                'Паропанк/Стимпанк',
                'Повседневность',
                'Полицейский боевик',
                'Полиция',
                'Постапокалиптика',
                'Приключения',
                'Психологический',
                'Психологический триллер',
                'Реверс-гарем',
                'Романтика',
                'Самураи',
                'Самурайский боевик (тямбара)',
                'Сверхъестественное',
                'Сёдзё-ай',
                'Сёнэн-ай',
                'Сказка',
                'Спокон',
                'Сэнтай',
                'Токусацу',
                'Триллер',
                'Ужасы',
                'Фантастика',
                'Фэнтези',
                'Школа',
                'Школьный детектив',
                'Экшн'
        }
        gn: str
        for gn in _genres_pattern:
            try:
                Genre.objects.create(title=gn)
            except IntegrityError as e:
                print(f'Жанр {gn} уже существует')

    def create_animes(self) -> None:
        anilist = Anilist()
        genre: QuerySet[Genre] = Genre.objects.all()
        decript: str = ''.join((random.choice(ascii_letters) for x in range(20)))
        rate_float: float = random.uniform(2,10)
        rates: float = float('{:.2f}'.format(rate_float))
        for i in range(116830, 126830):
            try:
                
                # names = str(name['name_romaji'])
                temp_anime: Anime = Anime.objects.create(
                    title = anilist.get_anime_with_id(i).get['name_romaji'],
                    description = decript,
                    rate = rates,
                    genres = random.choice(genre)
                )
                temp_anime.save()
            except Exception as e:
                pass
            

    def handle(self, *args, **kwargs):
        # self.create_genres()
        self.create_animes()
        print("FINISH")