# Generated by Django 5.1.6 on 2025-03-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_menuitem_order_price_alter_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
