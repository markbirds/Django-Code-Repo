# Generated by Django 3.1.1 on 2020-09-19 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0007_auto_20200919_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.user'),
        ),
    ]
