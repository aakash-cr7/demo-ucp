from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Create your models here.
ROLE_CHOICES =  (
    ('STAFF', 'staff'),
    ('STUDENT', 'stud'),
    ('MODERATOR', 'mod')
)
PROGRAM_CHOICES = (
    ('BTech', 'BT'),
    ('MTech', 'MT'),
    ('BBA', 'BBA'),
    ('MBA', 'MBA'),
)


class CustomUser(AbstractUser):
    role = models.CharField(max_length = 100, choices = ROLE_CHOICES, default = ROLE_CHOICES[0][1])
    last_login_at = models.DateTimeField(auto_now = True)
    phone_number = models.CharField(max_length = 10, null = True)
    display_picture = models.ImageField(upload_to = 'profile_pics/', blank = True, null = True)
    is_email_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'CustomUser'
        unique_together = ('email',)

class Student(CustomUser):
    # ?
    yr_of_passing = models.CharField(max_length = 4, null = True, blank = True)
    is_alumni = models.BooleanField(default = False)
    program = models.CharField(choices = PROGRAM_CHOICES, max_length = 100, null = True, blank = True)
    enrollment_number = models.PositiveIntegerField()
    fav_category = models.ManyToManyField('Category', blank = True)
    resume = models.FileField(blank = True)
    skills = models.ManyToManyField('Category', blank = True, related_name = 'students_skills')
    website_url = models.URLField(blank = True)
    number_of_semesters = models.PositiveIntegerField(blank = True, null = True)
    is_reported = models.BooleanField(default = False)
    reported_by = models.OneToOneField('Moderator', null = True, blank=True)
    is_reported_to_admin = models.BooleanField(default = False)


    class Meta:
        verbose_name = 'Student'


class Staff(CustomUser):
    staff_id = models.PositiveIntegerField()
    fav_category = models.ManyToManyField('Category', blank = True)

    class Meta:
        verbose_name = 'Staff'


class Moderator(CustomUser):
    moderator_id = models.PositiveIntegerField()
    fav_category = models.ManyToManyField('Category', blank = True)

    class Meta:
        verbose_name = 'Moderator'

class Category(models.Model):
    name = models.CharField(max_length = 254)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)
