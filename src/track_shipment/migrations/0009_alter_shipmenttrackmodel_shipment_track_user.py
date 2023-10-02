# Generated by Django 4.2.4 on 2023-10-01 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('track_shipment', '0008_alter_shipmenttrackmodel_shipment_track_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmenttrackmodel',
            name='shipment_track_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]