# Generated by Django 5.1.3 on 2024-11-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_selleritems_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleritems',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
    ]
