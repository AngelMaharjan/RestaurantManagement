# Generated by Django 4.1.7 on 2023-04-30 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "ForkAndKnife",
            "0002_remove_orderitem_product_remove_billing_orderr_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(name="Billing",),
    ]
