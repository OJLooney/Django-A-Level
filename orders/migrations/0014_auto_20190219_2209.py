# Generated by Django 2.1.1 on 2019-02-19 22:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0013_myuserordering'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUserOrdering',
            new_name='MyOrderOrdering',
        ),
    ]
