# Generated by Django 3.2.2 on 2021-05-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_mail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]