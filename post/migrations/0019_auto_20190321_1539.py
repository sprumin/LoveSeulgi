# Generated by Django 2.0 on 2019-03-21 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20190321_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='thumbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 39, 18, 986995)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 39, 18, 985998)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 39, 18, 986995)),
        ),
    ]
