# Generated by Django 4.1.7 on 2023-03-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_listing_listing_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_categories',
            field=models.CharField(choices=[('CL', 'Clothing'), ('SH', 'Shoes'), ('AC', 'Accessories'), ('OT', 'Other')], default='OT', max_length=2),
        ),
    ]
