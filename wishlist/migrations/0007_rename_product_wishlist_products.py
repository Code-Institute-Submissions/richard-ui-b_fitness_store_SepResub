# Generated by Django 3.2 on 2021-08-18 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0006_remove_wishlist_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='product',
            new_name='products',
        ),
    ]