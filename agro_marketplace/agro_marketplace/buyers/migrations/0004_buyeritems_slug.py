# Generated by Django 5.1.3 on 2024-11-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0003_buyeritems_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyeritems',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
    ]