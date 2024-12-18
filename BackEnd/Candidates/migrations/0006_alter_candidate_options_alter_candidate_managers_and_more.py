# Generated by Django 4.2 on 2024-11-08 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0005_remove_candidate_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={},
        ),
        migrations.AlterModelManagers(
            name='candidate',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='user_permissions',
        ),
    ]