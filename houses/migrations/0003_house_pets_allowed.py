# Generated by Django 4.1.4 on 2023-01-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pets_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
