# Generated by Django 2.2.14 on 2020-12-26 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201226_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='delay_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
