# Generated by Django 2.0 on 2019-03-18 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190318_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useralbum',
            old_name='test',
            new_name='photo',
        ),
    ]
