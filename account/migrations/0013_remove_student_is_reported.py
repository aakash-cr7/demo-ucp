# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_student_reported_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_reported',
        ),
    ]
