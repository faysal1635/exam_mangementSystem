# Generated by Django 3.2.2 on 2021-05-26 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210526_1628'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usersinfo',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usersinfo',
            name='last_login',
        ),
    ]
