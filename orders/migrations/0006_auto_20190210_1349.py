# Generated by Django 2.1.1 on 2019-02-10 13:49

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190210_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=account.models.MyUser, on_delete=django.db.models.deletion.CASCADE, related_name='MyUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
