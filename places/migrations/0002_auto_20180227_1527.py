# Generated by Django 2.0.2 on 2018-02-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotspot',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='hotspot',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
