# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='display_picture',
            field=models.ImageField(upload_to='profile_pics/', blank=True, null=True),
        ),
    ]
