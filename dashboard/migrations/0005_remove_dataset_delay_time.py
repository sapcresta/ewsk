# Generated by Django 2.2.14 on 2021-01-17 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210105_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='delay_time',
        ),
    ]
