# Generated by Django 4.2 on 2024-11-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobOffers', '0006_joboffer_expirationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='numtel',
            field=models.CharField(max_length=255, null=True),
        ),
    ]