# Generated by Django 5.1.3 on 2024-11-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('vegetables', 'Vegetables'), ('fruits', 'Fruits'), ('grain', 'Grain'), ('dairy_products', 'Dairy products'), ('mushrooms', 'Mushrooms'), ('herbs_spices', 'Herbs and spices'), ('grapes', 'Grapes'), ('bee_products', 'Bee products'), ('other', 'Other')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
    ]