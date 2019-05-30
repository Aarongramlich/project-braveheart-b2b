# Generated by Django 2.1.2 on 2019-05-30 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('request_form_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('metadata_key', models.TextField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('field', models.TextField(max_length=255)),
                ('label', models.TextField(max_length=255)),
                ('field_type', models.TextField(blank=True, max_length=255)),
                ('consumer_label', models.TextField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('consumer_description', models.TextField(blank=True, max_length=255)),
                ('data_category', models.TextField(choices=[('personal', 'Personal Information'), ('commercial', 'Commercial Information'), ('biometric', 'Biometric Information'), ('internet', 'Internet Activity'), ('geolocation', 'Geolocation Information'), ('sensory', 'Sensory Information'), ('psychometric', 'Psychometric Information'), ('employment', 'Employment Information'), ('inferred', 'Inferred Information')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request_form_app.Company')),
            ],
        ),
    ]
