# Generated by Django 3.2 on 2022-09-05 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lname',
        ),
    ]
