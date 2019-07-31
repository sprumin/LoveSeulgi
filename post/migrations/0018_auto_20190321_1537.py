# Generated by Django 2.0 on 2019-03-21 06:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20190318_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('message', models.TextField(default='Comment')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 37, 32, 903504))),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 37, 32, 903504)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 37, 32, 904500)),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
