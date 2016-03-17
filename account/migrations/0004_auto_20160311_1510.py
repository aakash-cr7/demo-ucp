# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20160311_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='number_of_semesters',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
