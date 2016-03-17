# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('role', models.CharField(max_length=100, choices=[('STAFF', 'staff'), ('STUDENT', 'stud'), ('MODERATOR', 'mod')], default='staff')),
                ('last_login_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('customuser_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, auto_created=True)),
                ('moderator_id', models.CharField(max_length=100)),
                ('fav_category', models.ManyToManyField(to='account.Category', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('account.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('customuser_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, auto_created=True)),
                ('staff_id', models.CharField(max_length=100)),
                ('fav_category', models.ManyToManyField(to='account.Category', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('account.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customuser_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, auto_created=True)),
                ('yr_of_passing', models.CharField(max_length=4)),
                ('is_alumni', models.BooleanField(default=False)),
                ('program', models.CharField(max_length=100, choices=[('BTech', 'BT'), ('MTech', 'MT'), ('BBA', 'BBA'), ('MBA', 'MBA')])),
                ('enrollment_number', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='', blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('number_of_semesters', models.PositiveIntegerField(blank=True)),
                ('fav_category', models.ManyToManyField(to='account.Category', blank=True)),
                ('skills', models.ManyToManyField(related_name='students_skills', to='account.Category', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('account.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True),
        ),
    ]
