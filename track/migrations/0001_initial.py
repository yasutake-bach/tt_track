# Generated by Django 4.1.5 on 2023-01-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boarding_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording_start_date', models.DateField()),
                ('recording_end_date', models.DateField()),
                ('distance', models.IntegerField(default=0)),
                ('duration', models.TimeField()),
                ('title', models.CharField(max_length=30)),
                ('height', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plotting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
