# Generated by Django 3.2.5 on 2021-09-20 15:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0005_alter_restaurant_max_number_of_people_for_reservation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TableReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_time', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='breakfast', max_length=50)),
                ('num_of_people', models.IntegerField(default=1)),
                ('reserved_date', models.DateTimeField(blank=True)),
                ('customer_arrival', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant')),
            ],
        ),
    ]
