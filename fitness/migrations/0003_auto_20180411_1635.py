# Generated by Django 2.0.2 on 2018-04-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_auto_20180411_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
