# Generated by Django 4.1.7 on 2023-03-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='listing_pics'),
        ),
    ]
