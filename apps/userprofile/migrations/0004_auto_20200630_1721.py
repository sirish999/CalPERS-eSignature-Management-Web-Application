# Generated by Django 3.0.7 on 2020-06-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_profile_signature_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signature_store',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
