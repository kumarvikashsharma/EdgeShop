# Generated by Django 4.0.1 on 2022-01-17 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='roduct',
            new_name='product',
        ),
    ]
