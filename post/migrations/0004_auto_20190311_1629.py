# Generated by Django 2.0 on 2019-03-11 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190311_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 16, 29, 43, 950000)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 16, 29, 43, 950997)),
        ),
    ]
