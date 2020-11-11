# Generated by Django 2.1.1 on 2019-03-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20190222_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='multiplier',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('0', 'Small'), ('1', 'Medium'), ('2', 'Large')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
