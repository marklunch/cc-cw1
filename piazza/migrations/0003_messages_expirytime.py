# Generated by Django 3.0.2 on 2021-02-17 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0002_messages_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='expiryTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 21, 33, 4, 453073)),
        ),
    ]
