# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='genre',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
