# Generated by Django 4.0.5 on 2022-06-13 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_event_finish_date_remove_event_media_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]