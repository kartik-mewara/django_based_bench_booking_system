# Generated by Django 3.0.8 on 2021-05-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bench4', '0002_auto_20210518_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation4',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
