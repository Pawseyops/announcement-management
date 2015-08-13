# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0003_announcement_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='Service',
            new_name='services',
        ),
    ]
