# Generated by Django 5.0 on 2023-12-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='mode_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
