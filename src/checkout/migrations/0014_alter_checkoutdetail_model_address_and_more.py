# Generated by Django 4.2.2 on 2023-08-23 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_alter_checkoutdetail_model_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 19, 24, 0, 876901, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='payment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='zipcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
