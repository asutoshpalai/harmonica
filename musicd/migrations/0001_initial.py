# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('uploaded', models.FileField(upload_to='')),
            ],
        ),
    ]
