# Generated by Django 3.1 on 2020-10-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20201018_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='getassured_attemptno',
            field=models.IntegerField(default=1),
        ),
    ]
