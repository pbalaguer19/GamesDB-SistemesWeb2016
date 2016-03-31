# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('abbreviation', models.TextField(null=True, blank=True)),
                ('city', models.TextField(max_length=100, null=True, blank=True)),
                ('mail', models.TextField(max_length=50, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('release_year', models.IntegerField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('price', models.IntegerField(null=True, blank=True)),
                ('release_year', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name=b'Rating (stars)', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('publish_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyGames',
            fields=[
                ('company_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Company')),
            ],
            bases=('gamesApp.company',),
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Review')),
            ],
            bases=('gamesApp.review',),
        ),
        migrations.CreateModel(
            name='GenreGames',
            fields=[
                ('genre_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Genre')),
            ],
            bases=('gamesApp.genre',),
        ),
        migrations.CreateModel(
            name='PlatformGames',
            fields=[
                ('platform_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Platform')),
            ],
            bases=('gamesApp.platform',),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='companies',
            field=models.ManyToManyField(to='gamesApp.Company'),
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='gamesApp.Genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(to='gamesApp.Platform'),
        ),
        migrations.AddField(
            model_name='game',
            name='reviews',
            field=models.ManyToManyField(to='gamesApp.Review'),
        ),
        migrations.AddField(
            model_name='game',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='platformgames',
            name='games',
            field=models.ManyToManyField(to='gamesApp.Game', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='genregames',
            name='games',
            field=models.ManyToManyField(to='gamesApp.Game', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gamereview',
            name='game',
            field=models.ForeignKey(to='gamesApp.Game'),
        ),
        migrations.AddField(
            model_name='companygames',
            name='games',
            field=models.ManyToManyField(to='gamesApp.Game', null=True, blank=True),
        ),
    ]
