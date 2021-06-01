from django.contrib import admin

from .models import Student,UsersInfo,Faculty,Admin
# Register your models here
admin.site.register(Student)
admin.site.register(UsersInfo)
admin.site.register(Faculty)
admin.site.register(Admin)
