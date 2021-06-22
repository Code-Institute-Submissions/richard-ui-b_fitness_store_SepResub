# Generated by Django 3.2 on 2021-06-22 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_list', '0002_alter_reviews_list_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews_list',
            name='rating',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
