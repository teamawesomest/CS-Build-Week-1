# Generated by Django 2.2.7 on 2019-11-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='y',
            field=models.IntegerField(default=0),
        ),
    ]
