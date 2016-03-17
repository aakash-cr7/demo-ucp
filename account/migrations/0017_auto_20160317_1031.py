# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20160317_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(max_length=100, null=True, choices=[('BTech', 'BT'), ('MTech', 'MT'), ('BBA', 'BBA'), ('MBA', 'MBA')], blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='yr_of_passing',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
