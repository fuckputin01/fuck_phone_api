# Generated by Django 4.0.3 on 2022-03-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_int',
            field=models.BigIntegerField(unique=True),
        ),
    ]
