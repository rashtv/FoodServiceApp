# Generated by Django 3.2.16 on 2023-05-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20230510_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
