# Generated by Django 4.2.7 on 2023-11-24 07:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('address', models.CharField(blank=True, max_length=100)),
                ('area', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('city', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('temperature', models.FloatField(blank=True)),
                ('feels_like', models.FloatField(blank=True)),
                ('temp_min', models.FloatField(blank=True)),
                ('temp_max', models.FloatField(blank=True)),
                ('pressure', models.IntegerField(blank=True)),
                ('humidity', models.IntegerField(blank=True)),
                ('main', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('icon', models.CharField(blank=True, max_length=10)),
                ('wind_speed', models.FloatField(blank=True)),
                ('wind_deg', models.IntegerField(blank=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('area', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
