# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0004_auto_20150728_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='services',
            new_name='service',
        ),
    ]
