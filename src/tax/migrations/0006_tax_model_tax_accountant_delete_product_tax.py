# Generated by Django 4.2.4 on 2023-09-26 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tax', '0005_remove_tax_model_total_service_charges_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax_model',
            name='tax_accountant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_tax_accountant', to=settings.AUTH_USER_MODEL, verbose_name='Tax Accountant'),
        ),
        migrations.DeleteModel(
            name='Product_Tax',
        ),
    ]
