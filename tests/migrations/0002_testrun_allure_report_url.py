# Generated by Django 5.2 on 2025-04-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrun',
            name='allure_report_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
