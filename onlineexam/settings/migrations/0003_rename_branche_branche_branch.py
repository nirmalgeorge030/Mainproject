# Generated by Django 4.2.4 on 2023-10-11 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_delete_master_data_rename_batch_batch_batch_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branche',
            old_name='branche',
            new_name='branch',
        ),
    ]
