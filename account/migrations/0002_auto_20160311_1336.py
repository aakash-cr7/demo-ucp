# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'CustomUser'},
        ),
        migrations.AlterModelOptions(
            name='moderator',
            options={'verbose_name': 'Moderator'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Staff'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student'},
        ),
    ]
