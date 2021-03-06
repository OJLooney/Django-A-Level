# Generated by Django 2.1.1 on 2019-04-26 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20190402_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrderItemOrdering',
            fields=[
                ('orderitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.OrderItem')),
                ('attributeChosen', models.CharField(choices=[('0', 'Order id'), ('1', 'Status: Preparing'), ('2', 'Status: Baking'), ('3', 'Status: Ready')], max_length=1)),
                ('OrderOfOrders', models.CharField(choices=[('0', 'Ascending'), ('1', 'Descending')], max_length=1)),
            ],
            bases=('orders.orderitem',),
        ),
    ]
