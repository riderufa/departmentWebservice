# Generated by Django 3.1.4 on 2020-12-14 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201214_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
