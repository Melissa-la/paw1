# Generated by Django 4.1.7 on 2023-11-11 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0005_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]