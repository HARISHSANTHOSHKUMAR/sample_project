# Generated by Django 4.1.5 on 2023-02-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0018_cart_usernme'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='usernme',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
    ]
