# Generated by Django 2.2.5 on 2019-09-25 18:07

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
