# Generated by Django 2.0.2 on 2018-04-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise', models.CharField(max_length=255)),
                ('weight', models.CharField(blank=True, max_length=255)),
                ('reps', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
