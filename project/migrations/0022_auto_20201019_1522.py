# Generated by Django 3.1 on 2020-10-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20201019_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='getassured_attemptno',
        ),
        migrations.AddField(
            model_name='response',
            name='getassured_attemptno',
            field=models.IntegerField(default=1),
        ),
    ]
