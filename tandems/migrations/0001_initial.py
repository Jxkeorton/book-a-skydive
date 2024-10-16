# Generated by Django 4.2.14 on 2024-09-25 18:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TandemDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('max_tandems', models.PositiveIntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='TandemTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('max_tandems', models.PositiveIntegerField(default=6)),
                ('booked_tandems', models.PositiveIntegerField(default=0)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeslots', to='tandems.tandemday')),
            ],
            options={
                'unique_together': {('day', 'time')},
            },
        ),
        migrations.CreateModel(
            name='VisitorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('height', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('full_name', models.CharField(max_length=100)),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tandem_timeslot', to='tandems.tandemtimeslot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tandem_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
