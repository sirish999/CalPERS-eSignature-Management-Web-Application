# Generated by Django 3.0.7 on 2020-07-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_profile_signature_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pref_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
