# Generated by Django 2.1.1 on 2019-02-22 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190220_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mycategoryordering',
            old_name='OrderOfProducts',
            new_name='OrderOfCategories',
        ),
    ]
