# Generated by Django 3.1.2 on 2020-10-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(help_text='Latitude for the squirrel')),
                ('Longitude', models.FloatField(help_text='Longitude for the squirrel')),
                ('Unique_Squirrel_ID', models.CharField(help_text='Identification tag for each squirrel sightings', max_length=100, unique=True)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=100)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=100)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=100)),
                ('Specific_Location', models.CharField(blank=True, max_length=100)),
                ('Running', models.BooleanField(blank=True)),
                ('Chasing', models.BooleanField(blank=True)),
                ('Climbing', models.BooleanField(blank=True)),
                ('Eating', models.BooleanField(blank=True)),
                ('Foraging', models.BooleanField(blank=True)),
                ('Other_Activities', models.CharField(blank=True, max_length=100)),
                ('Kuks', models.BooleanField(blank=True)),
                ('Quaas', models.BooleanField(blank=True)),
                ('Moans', models.BooleanField(blank=True)),
                ('Tail_Flags', models.BooleanField(blank=True)),
                ('Tail_Twitches', models.BooleanField(blank=True)),
                ('Approaches', models.BooleanField(blank=True)),
                ('Indifferent', models.BooleanField(blank=True)),
                ('Runs_From', models.BooleanField(blank=True)),
            ],
        ),
    ]
