# Generated by Django 2.2.3 on 2019-08-09 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 8, 31, 39, 751510)),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 8, 31, 39, 753635)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 8, 31, 39, 752148)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 8, 31, 39, 754176)),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 8, 31, 39, 753027)),
        ),
        migrations.AlterField(
            model_name='reportcomment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 8, 31, 39, 754800)),
        ),
    ]