# Generated by Django 4.0.3 on 2022-03-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_phone_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
