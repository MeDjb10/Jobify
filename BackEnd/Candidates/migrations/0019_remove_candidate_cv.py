# Generated by Django 4.2 on 2024-11-11 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0018_alter_resume_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='cv',
        ),
    ]