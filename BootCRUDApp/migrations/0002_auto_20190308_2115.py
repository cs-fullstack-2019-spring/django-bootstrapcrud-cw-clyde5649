# Generated by Django 2.0.6 on 2019-03-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootCRUDApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garagesellmodel',
            name='price',
            field=models.IntegerField(default=''),
        ),
    ]
