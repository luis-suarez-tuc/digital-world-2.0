# Generated by Django 5.0.7 on 2024-08-22 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specifications',
        ),
    ]
