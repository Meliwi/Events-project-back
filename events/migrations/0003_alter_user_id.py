# Generated by Django 4.0.4 on 2022-06-11 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_id_event_news_id_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
