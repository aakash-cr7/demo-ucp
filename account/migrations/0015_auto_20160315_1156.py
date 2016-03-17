# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_student_is_reported_to_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_reported_to_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='reported_by',
            field=models.OneToOneField(to='account.Moderator', null=True),
        ),
    ]
