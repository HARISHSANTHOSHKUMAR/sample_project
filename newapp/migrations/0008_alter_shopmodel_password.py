# Generated by Django 4.1.5 on 2023-01-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_shopmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopmodel',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
