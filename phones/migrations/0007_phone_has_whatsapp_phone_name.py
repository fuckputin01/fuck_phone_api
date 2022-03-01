# Generated by Django 4.0.3 on 2022-03-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_alter_phone_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='has_whatsapp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
