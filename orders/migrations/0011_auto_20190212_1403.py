# Generated by Django 2.1.1 on 2019-02-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20190212_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderType',
            field=models.CharField(choices=[('s', 'in store'), ('d', 'delivery'), ('c', 'collection')], default='s', help_text='\nChoose Delivery, Collection or In Store.', max_length=1),
        ),
    ]
