# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20160311_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='moderator_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment_number',
            field=models.PositiveIntegerField(),
        ),
    ]
