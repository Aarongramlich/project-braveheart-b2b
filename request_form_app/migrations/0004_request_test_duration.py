# Generated by Django 2.1.2 on 2019-06-11 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_form_app', '0003_auto_20190608_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='test_duration',
            field=models.DurationField(default=datetime.timedelta),
        ),
    ]
