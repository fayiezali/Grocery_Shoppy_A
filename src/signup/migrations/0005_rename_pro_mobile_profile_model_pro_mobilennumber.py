# Generated by Django 4.2.2 on 2023-07-17 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_rename_profilemodel_profile_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_model',
            old_name='Pro_Mobile',
            new_name='Pro_MobileNnumber',
        ),
    ]
