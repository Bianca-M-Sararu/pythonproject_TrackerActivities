# Generated by Django 5.0.1 on 2024-01-04 16:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_activitati_rating_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitati',
            name='rating_intensity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
