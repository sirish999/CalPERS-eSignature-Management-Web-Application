# Generated by Django 3.0.7 on 2020-06-30 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_profile_signature_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='signature_store',
        ),
    ]
