# Generated by Django 3.1 on 2020-10-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0026_auto_20201020_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='activate',
            field=models.IntegerField(default=0),
        ),
    ]
