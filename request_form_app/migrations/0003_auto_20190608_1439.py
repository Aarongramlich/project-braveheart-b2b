# Generated by Django 2.1.2 on 2019-06-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_form_app', '0002_company_legal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='legal_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
