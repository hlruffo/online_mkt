# Generated by Django 3.2.18 on 2023-03-22 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20230322_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='categoty',
            new_name='category',
        ),
    ]
