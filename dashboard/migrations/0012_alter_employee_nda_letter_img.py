# Generated by Django 3.2 on 2022-09-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20220901_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='NDA_letter_img',
            field=models.BooleanField(max_length=50, null=True),
        ),
    ]
