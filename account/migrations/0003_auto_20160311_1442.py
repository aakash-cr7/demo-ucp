# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160311_1336'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together=set([('email',)]),
        ),
    ]
