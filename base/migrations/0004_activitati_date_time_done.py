# Generated by Django 5.0.1 on 2024-01-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_activitati_options_topic_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitati',
            name='date_time_done',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
