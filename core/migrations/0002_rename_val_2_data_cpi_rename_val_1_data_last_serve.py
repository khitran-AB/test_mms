# Generated by Django 4.0.6 on 2022-08-31 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='val_2',
            new_name='cpi',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='val_1',
            new_name='last_serve',
        ),
    ]
