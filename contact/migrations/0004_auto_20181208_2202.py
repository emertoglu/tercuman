# Generated by Django 2.0.3 on 2018-12-08 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20181208_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='from_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='full_name',
        ),
    ]
