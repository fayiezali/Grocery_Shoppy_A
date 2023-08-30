# Generated by Django 4.2.2 on 2023-08-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0006_rename_price_tax_model_tax_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tax_model',
            options={'ordering': ('-tax',), 'verbose_name': 'Tax', 'verbose_name_plural': 'Taxs'},
        ),
        migrations.AlterField(
            model_name='tax_model',
            name='tax',
            field=models.PositiveIntegerField(blank=True, default=15, null=True, verbose_name='Tax %'),
        ),
    ]