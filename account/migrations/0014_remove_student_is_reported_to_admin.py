# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_student_is_reported'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_reported_to_admin',
        ),
    ]
