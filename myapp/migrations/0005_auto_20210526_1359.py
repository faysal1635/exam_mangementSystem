# Generated by Django 3.2.2 on 2021-05-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_student_login_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersInfo',
            fields=[
                ('login_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=12, null=True)),
                ('type', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'users_info',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'managed': False},
        ),
    ]
