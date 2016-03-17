# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160311_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='moderator_id',
            field=models.PositiveIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.PositiveIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment_number',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]
