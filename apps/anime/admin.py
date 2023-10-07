# Python
from typing import Optional

# Django
from django.contrib import admin

# Local
from .models import (
    Genre,
    Anime,
    Season,
    Episode,
    Comment,
)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    GenreAdmin admin.
    """
    readonly_fields = ()


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """
    AnimeAdmin admin.
    """
    readonly_fields = ()


@admin.register(Season)
class SeasonTypeAdmin(admin.ModelAdmin):
    """
    SeasonAdmin admin.
    """
    readonly_fields = ()

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    """
    EpisodeAdmin admin.
    """
    readonly_fields = ()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    CommentAdmin admin.
    """
    readonly_fields = ()