# Generated by Django 2.2.1 on 2019-07-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190711_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='votes_total',
        ),
    ]
