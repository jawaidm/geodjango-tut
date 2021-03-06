# Generated by Django 3.2.10 on 2022-01-11 13:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_alter_worldborder_fips'),
    ]

    operations = [
        migrations.CreateModel(
            name='DpawRegion',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=64)),
                ('ogc_fid', models.IntegerField(blank=True, null=True)),
                ('office', models.CharField(blank=True, max_length=64, null=True)),
                ('hectares', models.FloatField(blank=True, null=True)),
                ('md5_rowhash', models.CharField(blank=True, max_length=64, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4283)),
            ],
        ),
    ]
