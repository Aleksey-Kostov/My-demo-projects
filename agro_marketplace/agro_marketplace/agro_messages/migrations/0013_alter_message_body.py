# Generated by Django 5.1.3 on 2024-11-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro_messages', '0012_alter_message_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
