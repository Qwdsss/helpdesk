# Generated by Django 4.2.5 on 2023-10-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk_app', '0003_problem_assigned_user_problem_resolved_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='assigned_user',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='resolved_user',
        ),
    ]
