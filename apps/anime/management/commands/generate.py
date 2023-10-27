# PYTHON
import requests
import random
import datetime
from typing import Any, Optional
from string import ascii_letters
#DRF
from django.core.management import BaseCommand
from django.db.models.query import QuerySet
from django.db.utils import IntegrityError
#LOCAL
from anime.models import (
    Genre,
    Anime
)
from abstracts.set_list import ANIME, GENRES


class Command(BaseCommand):
    """Command for generate data for Database."""

    def create_genres(self) -> None:
        _genres_pattern: set[str] = GENRES
        gn: str
        for gn in _genres_pattern:
            try:
                Genre.objects.create(title=gn)
            except IntegrityError as e:
                print(f'Жанр {gn} уже существует')

    def create_animes(self) -> None:
        for i in range(10):
            decript: str = ''.join((random.choice(ascii_letters) for x in range(random.randint(10,30))))
            genres = Genre.objects.all()
            rate_float: float = random.uniform(1,10)
            rates: float = float('{:.2f}'.format(rate_float))
<<<<<<< HEAD
=======
            # a = list(ANIME)
>>>>>>> 050cb8c (Permission)
            an = ''.join(x for x in random.choice(list(ANIME)))
            try:
                temp_anime: Anime = Anime.objects.create(
                    title = an,
                    description = decript,
                    rate = rates
                )
                for _ in range(random.randint(0, 5)):
                    temp_anime.genres.add(
                        random.choice(genres)
                    )
                temp_anime.save()
            except Exception as e:
                print(f"EXC ->> {e}")
            

    def handle(self, *args, **kwargs):
        # self.create_genres()
        self.create_animes()
        print("FINISH")