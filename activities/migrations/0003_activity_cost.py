# Generated by Django 4.0.5 on 2022-08-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activity_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='Cost',
            field=models.FloatField(default=1000),
        ),
    ]
