# Generated by Django 2.0 on 2019-03-11 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20190311_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 19, 11, 6, 621567)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 19, 11, 6, 622565)),
        ),
    ]
