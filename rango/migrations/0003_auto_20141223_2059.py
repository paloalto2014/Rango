# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20141223_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='likes',
            new_name='like',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='views',
            new_name='view',
        ),
    ]
