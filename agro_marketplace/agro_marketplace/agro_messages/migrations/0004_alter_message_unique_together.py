# Generated by Django 5.1.3 on 2024-11-23 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agro_messages', '0003_message_parent_message'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set(),
        ),
    ]
