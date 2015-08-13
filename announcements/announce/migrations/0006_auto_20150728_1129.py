# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0005_auto_20150728_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='withdrawn',
            new_name='inactive',
        ),
    ]
