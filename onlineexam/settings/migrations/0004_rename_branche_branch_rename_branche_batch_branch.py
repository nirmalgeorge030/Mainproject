# Generated by Django 4.2.4 on 2023-10-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_rename_branche_branche_branch'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Branche',
            new_name='Branch',
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='Branche',
            new_name='Branch',
        ),
    ]
