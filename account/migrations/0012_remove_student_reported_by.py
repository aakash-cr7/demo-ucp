# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20160315_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='reported_by',
        ),
    ]
