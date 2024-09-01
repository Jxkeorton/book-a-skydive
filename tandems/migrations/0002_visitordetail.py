# Generated by Django 4.2.14 on 2024-09-01 16:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tandems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('height', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('full_name', models.CharField(max_length=100)),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_details', to='tandems.tandemtimeslot')),
            ],
        ),
    ]
