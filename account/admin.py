from django.contrib import admin
from .models import CustomUser, Student, Staff, Moderator, Category

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Moderator)
admin.site.register(Category)
