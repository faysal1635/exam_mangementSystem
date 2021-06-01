from django.db import models
# Create your models here.


class Student(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=12)
    login_id = models.CharField(max_length=12)
    stu_name = models.CharField(max_length=12, blank=True, null=True)
    stu_level = models.CharField(max_length=10, blank=True, null=True)
    stu_dept = models.CharField(max_length=12, blank=True, null=True)
    stu_mail = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'
        unique_together = (('stu_id', 'login_id'),)


class UsersInfo(models.Model):
    login_id = models.CharField(primary_key=True, max_length=12)
    password = models.CharField(max_length=12, blank=True, null=True)
    type = models.CharField(max_length=12, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'users_info'


class Faculty(models.Model):
    fac_id = models.CharField(primary_key=True, max_length=12)
    login_id = models.CharField(max_length=12)
    fac_name = models.CharField(max_length=12, blank=True, null=True)
    fac_mail = models.CharField(max_length=50, blank=True, null=True)
    fac_phone_no = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'faculty'
        unique_together = (('fac_id', 'login_id'),)


class Admin(models.Model):
    login_id = models.CharField(max_length=12)
    admin_id = models.CharField(primary_key=True, max_length=12)
    admin_name = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'admin'
        unique_together = (('admin_id', 'login_id'),)
