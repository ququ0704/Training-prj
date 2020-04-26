# Generated by Django 3.0.5 on 2020-04-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20200425_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coder',
            name='todo_list',
        ),
        migrations.RemoveField(
            model_name='coder',
            name='user',
        ),
        migrations.AddField(
            model_name='coder',
            name='password',
            field=models.CharField(default='123456', max_length=30),
        ),
        migrations.AddField(
            model_name='coder',
            name='username',
            field=models.CharField(default='jason', max_length=30),
        ),
        migrations.AddField(
            model_name='todolist',
            name='coder',
            field=models.ManyToManyField(to='todolist.Coder'),
        ),
    ]
