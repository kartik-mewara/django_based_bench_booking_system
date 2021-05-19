# Generated by Django 3.0.8 on 2021-05-16 06:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0002_auto_20200705_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EventMember',
        ),
    ]
