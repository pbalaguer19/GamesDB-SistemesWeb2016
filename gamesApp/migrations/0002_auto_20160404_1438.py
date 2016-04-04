# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gamesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyGame',
            fields=[
                ('company_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Company')),
            ],
            bases=('gamesApp.company',),
        ),
        migrations.CreateModel(
            name='GenreGame',
            fields=[
                ('genre_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Genre')),
            ],
            bases=('gamesApp.genre',),
        ),
        migrations.CreateModel(
            name='PlatformGame',
            fields=[
                ('platform_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gamesApp.Platform')),
            ],
            bases=('gamesApp.platform',),
        ),
        migrations.RemoveField(
            model_name='companygames',
            name='company_ptr',
        ),
        migrations.RemoveField(
            model_name='companygames',
            name='games',
        ),
        migrations.RemoveField(
            model_name='genregames',
            name='games',
        ),
        migrations.RemoveField(
            model_name='genregames',
            name='genre_ptr',
        ),
        migrations.RemoveField(
            model_name='platformgames',
            name='games',
        ),
        migrations.RemoveField(
            model_name='platformgames',
            name='platform_ptr',
        ),
        migrations.AlterField(
            model_name='game',
            name='reviews',
            field=models.ManyToManyField(to='gamesApp.Review', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='CompanyGames',
        ),
        migrations.DeleteModel(
            name='GenreGames',
        ),
        migrations.DeleteModel(
            name='PlatformGames',
        ),
        migrations.AddField(
            model_name='platformgame',
            name='games',
            field=models.ManyToManyField(to='gamesApp.Game', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='genregame',
            name='games',
            field=models.ManyToManyField(to='gamesApp.Game', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companygame',
            name='games',
            field=models.ManyToManyField(to='gamesApp.Game', null=True, blank=True),
        ),
    ]
