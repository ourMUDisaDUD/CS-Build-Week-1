# Generated by Django 2.2.5 on 2019-09-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20190925_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='key',
            field=models.IntegerField(default=0),
        ),
    ]