# Generated by Django 4.1.7 on 2023-03-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_comment_author'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='comment',
            constraint=models.UniqueConstraint(fields=('author',), name='unique_user_comment'),
        ),
    ]
