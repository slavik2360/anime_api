# Python
import datetime

# django
from django.db import models
# from django_extensions.db.fields import FileTypeField, FileTypeValidator
# from django_extensions.validators import FileTypeField, FileTypeValidator
from django.core.validators import FileExtensionValidator


#Local
from auths.models import MyUser


class Genre(models.Model):
    """
    Model Anime Genre.
    """

    title = models.CharField(
        verbose_name='название жанра',
        max_length=130,
        unique=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self) -> str:
        return self.title


class Anime(models.Model):
    """
    Model Anime.
    """
    def default_poster():
        return '/default/poster.jpg'

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
        validators=[FileExtensionValidator(
            allowed_extensions=[
                'png', 'jpg', 'jpeg',
                'gif'
            ],
            message='Sorry, this file format is not supported'
        )],
        default=default_poster(),
        blank=True
    )
    genres = models.ManyToManyField(
        verbose_name='жанры',
        to=Genre,
        related_name='animes'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'аниме'
        verbose_name_plural = 'аниме'

    def __str__(self) -> str:
        rate_star = int(self.rate) * '☆'
        return f"{self.title} | {rate_star}"


class Season(models.Model):
    """
    Model Anime Season.
    """
    anime = models.ForeignKey(
        to=Anime, 
        verbose_name='какое аниме',
        related_name='seasons', 
        on_delete=models.CASCADE
    )
    season_number = models.IntegerField(
        verbose_name='какой сезон аниме'
    )

    class Meta:
        ordering = ('anime',)
        verbose_name = 'сезон'
        verbose_name_plural = 'сезоны'

    def __str__(self) -> str:
        return f'{self.anime.title} | сезон: {self.season_number}'

class Episode(models.Model):
    """
    Model Anime Episode.
    """
    season = models.ForeignKey(
        to=Season,
        related_name='episodes', 
        on_delete=models.CASCADE
    )
    episode_number: int = models.IntegerField(
        verbose_name='номер эпизода'
    )
    title: str = models.CharField(
        verbose_name='название эпизода',
        max_length=120
    )
    video: str = models.FileField(
        verbose_name='видео',
        upload_to='videos/%Y/',
        validators=[FileExtensionValidator(
            allowed_extensions=[
                'mp4', 'avi', 'mkv',
                'mov',
                # для теста 
                'png', 'jpg', 'jpeg',
                'gif', 'svg'
            ],
            message='Sorry, this file format is not supported'
        )],
        null=True,
        blank=True   
    )
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'серии'
        verbose_name_plural = 'серии'

    def __str__(self) -> str:
        return f'{self.season.anime.title} | серия: {self.episode_number}'


class Comment(models.Model):
    """
    Model Comment to Anime.
    """
    user = models.ForeignKey(
        verbose_name='кто оставил',
        to=MyUser,
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
        return f'{self.user.nickname} | {self.anime.title}'
    


# class VideoFileType(models.Model):
#     """
#     Модель для хранения типов расширений видео-файлов.
#     """
#     name: models.CharField = models.CharField(
#         verbose_name='название',
#         max_length=10
#     )

#     class Meta:
#         verbose_name = 'тип расширения видео-файла'
#         verbose_name_plural = 'типы расширений видео-файлов'

#     def __str__(self):
#         return f'Расширение: {self.name}'