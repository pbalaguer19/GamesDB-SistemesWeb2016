# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesApp', '0002_auto_20160404_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companygame',
            name='company_ptr',
        ),
        migrations.RemoveField(
            model_name='companygame',
            name='games',
        ),
        migrations.RemoveField(
            model_name='genregame',
            name='games',
        ),
        migrations.RemoveField(
            model_name='genregame',
            name='genre_ptr',
        ),
        migrations.RemoveField(
            model_name='platformgame',
            name='games',
        ),
        migrations.RemoveField(
            model_name='platformgame',
            name='platform_ptr',
        ),
        migrations.AlterField(
            model_name='game',
            name='companies',
            field=models.ManyToManyField(related_name='games', to='gamesApp.Company'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(related_name='games', to='gamesApp.Genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(related_name='games', to='gamesApp.Platform'),
        ),
        migrations.DeleteModel(
            name='CompanyGame',
        ),
        migrations.DeleteModel(
            name='GenreGame',
        ),
        migrations.DeleteModel(
            name='PlatformGame',
        ),
    ]
