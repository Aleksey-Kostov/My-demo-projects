# Generated by Django 5.1.3 on 2024-11-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selleritems',
            name='unit_of_measure',
            field=models.CharField(choices=[('pc', 'Pieces'), ('kg', 'Kilograms'), ('l', 'Liters'), ('m', 'Meters'), ('bx', 'Boxes'), ('t', 'Tons')], default='kg', max_length=3),
        ),
    ]
