# Generated by Django 3.0.8 on 2020-07-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200711_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
