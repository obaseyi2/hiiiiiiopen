# Generated by Django 5.0.6 on 2024-09-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0006_alter_product_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, choices=[('school hostel', 'School Hostel'), ('gate', 'Gate'), ('agbede', 'Agbede'), ('kofesu', 'Kofesu'), ('harmony', 'Harmony'), ('accord', 'Accord'), ('zoo', 'Zoo'), ('oluwo', 'Oluwo'), ('isolu', 'Isolu'), ('camp', 'Camp')], max_length=50),
        ),
    ]
