# Generated by Django 2.0 on 2019-03-26 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20190322_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcomment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 15, 37, 26, 488859)),
        ),
    ]
