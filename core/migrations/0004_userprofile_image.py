# Generated by Django 3.1.4 on 2020-12-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201214_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/%Y/%m/%d', verbose_name='Фотография'),
        ),
    ]
