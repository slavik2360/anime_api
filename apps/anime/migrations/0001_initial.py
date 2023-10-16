# Generated by Django 4.2.5 on 2023-10-07 08:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название аниме')),
                ('description', models.CharField(max_length=300, verbose_name='описание')),
                ('rate', models.FloatField(max_length=5, verbose_name='рейтинг')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'gif'], message='Sorry, this file format is not supported')], verbose_name='постер')),
            ],
            options={
                'verbose_name': 'аниме',
                'verbose_name_plural': 'аниме',
                'ordering': ('-rate',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130, unique=True, verbose_name='название жанра')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_number', models.IntegerField(verbose_name='какой сезон аниме')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='anime.anime', verbose_name='какое аниме')),
            ],
            options={
                'verbose_name': 'сезон',
                'verbose_name_plural': 'сезоны',
                'ordering': ('anime',),
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_number', models.IntegerField(verbose_name='номер эпизода')),
                ('title', models.CharField(max_length=120, verbose_name='название эпизода')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%Y/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv', 'mov', 'png', 'jpg', 'jpeg', 'gif', 'svg'], message='Sorry, this file format is not supported')], verbose_name='видео')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='anime.season')),
            ],
            options={
                'verbose_name': 'сезон',
                'verbose_name_plural': 'сезоны',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=254, verbose_name='текст')),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anime_comments', to='anime.anime', verbose_name='аниме')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ('-id',),
            },
        ),
    ]