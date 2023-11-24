# Generated by Django 4.2.6 on 2023-11-24 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bed_type', models.CharField(choices=[('SI', 'Single'), ('DO', 'Double'), ('KS', 'King Size'), ('QS', 'Queen Size')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RoomFeature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('floor', models.PositiveIntegerField()),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('capacity', models.PositiveIntegerField()),
                ('is_occupied', models.BooleanField(default=False)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
                ('beds', models.ManyToManyField(blank=True, related_name='bed_rooms', to='rooms.bed')),
                ('features', models.ManyToManyField(blank=True, to='rooms.roomfeature')),
                ('promotions', models.ManyToManyField(blank=True, to='promotions.promotion')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
