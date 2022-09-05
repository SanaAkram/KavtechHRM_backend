# Generated by Django 3.2 on 2022-09-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='billing_currency',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='client_relation_start_comment',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='client_relation_start_date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='comment',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_address_line1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_address_line2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_bus_domain',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_1_email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_1_im',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_1_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_1_role',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_2_email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_2_im',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_2_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_2_role',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_3_email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_3_im',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_3_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_person_3_role',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='company_website',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='contact_person_1_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='contact_person_2_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='contact_person_3_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='referal_source',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
