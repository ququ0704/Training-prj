# Generated by Django 3.0.5 on 2020-04-25 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='title',
            new_name='tittle',
        ),
    ]
