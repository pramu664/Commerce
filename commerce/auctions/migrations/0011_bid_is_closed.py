# Generated by Django 4.1.7 on 2023-03-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
