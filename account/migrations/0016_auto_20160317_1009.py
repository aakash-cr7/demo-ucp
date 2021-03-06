# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20160315_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(max_length=100, choices=[('BTech', 'BT'), ('MTech', 'MT'), ('BBA', 'BBA'), ('MBA', 'MBA')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reported_by',
            field=models.OneToOneField(to='account.Moderator', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='yr_of_passing',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
