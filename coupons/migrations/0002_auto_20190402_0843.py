# Generated by Django 2.1.1 on 2019-04-02 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='valid_form',
            new_name='valid_from',
        ),
    ]