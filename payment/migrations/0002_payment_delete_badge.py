# Generated by Django 4.0.5 on 2022-08-03 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_delete_payment'),
        ('activities', '0003_activity_cost'),
        ('users', '0001_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Value', models.IntegerField()),
                ('pay_method', models.CharField(max_length=30)),
                ('ID_Activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
                ('ID_Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ID_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Badge',
        ),
    ]