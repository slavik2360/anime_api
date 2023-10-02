# Python
import datetime
# django
from django.db import models
from django.contrib.auth.models import User
# from apps.auths.models import MyUser


class Genre(models.Model):
    """Аниме жанры"""

    name = models.CharField(
        verbose_name='название жанра',
        max_length=130,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self) -> str:
        return self.name


class Anime(models.Model):
    """МОДЕЛЬ АНИМЕ"""

    title: str = models.CharField(
        verbose_name='название аниме',
        max_length=150
    )
    description: str = models.CharField(
        verbose_name='описание',
        max_length=300 # для программиста
    )
    rate: float = models.FloatField(
        verbose_name='рейтинг',
        max_length=5
    )
    poster: str = models.ImageField(
        verbose_name='постер',
        upload_to='posters',
        null=True
    )
    video: str = models.FileField(
        verbose_name='видео',
        upload_to='videos/%Y/',
        null=True,
        blank=True   
    )
    genres = models.ManyToManyField(
        verbose_name='жанры',
        to=Genre,
        related_name='animes'
    )

    class Meta:
        ordering = ('-rate',)
        verbose_name = 'аниме'
        verbose_name_plural = 'аниме'

    def __str__(self) -> str:
        rate = self.rate * '☆'
        return f"{self.title} | {self.rate}"


class VideoFileType(models.Model):
    """
    Модель для хранения типов расширений видео-файлов.
    """
    name: models.CharField = models.CharField(
        verbose_name='название',
        max_length=10
    )

    class Meta:
        verbose_name = 'тип расширения видео-файла'
        verbose_name_plural = 'типы расширений видео-файлов'

    def __str__(self):
        return f'Расширение: {self.name}'


class Comment(models.Model):
    """
    Комментарии к Аниме
    """
    
    user = models.ForeignKey(
        verbose_name='кто оставил',
        to=User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='текст',
        max_length=254
    )
    anime = models.ForeignKey(
        verbose_name='аниме',
        related_name='anime_comments',
        to=Anime,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self) -> str:
        return f'{self.user.username} | {self.anime.title}'