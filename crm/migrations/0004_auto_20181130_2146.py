# Generated by Django 2.0.3 on 2018-11-30 18:46

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_account_account_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Müşteri Number'),
        ),
    ]
