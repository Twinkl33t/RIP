# Generated by Django 3.1.4 on 2020-12-15 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201215_1942'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.DeleteModel(
            name='Processor',
        ),
    ]
