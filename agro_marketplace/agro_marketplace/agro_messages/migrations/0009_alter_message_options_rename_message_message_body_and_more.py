# Generated by Django 5.1.3 on 2024-11-27 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro_messages', '0008_messagereadstatus_is_deleted'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MessageStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='agro_messages.message')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_statuses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MessageReadStatus',
        ),
    ]
