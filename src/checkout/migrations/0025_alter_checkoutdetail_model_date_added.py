# Generated by Django 4.2.2 on 2023-08-28 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0024_alter_checkoutdetail_model_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 19, 8, 6, 23336, tzinfo=datetime.timezone.utc)),
        ),
    ]
