# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesApp', '0002_auto_20160504_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
    ]
