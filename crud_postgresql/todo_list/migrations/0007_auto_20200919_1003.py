# Generated by Django 3.1.1 on 2020-09-19 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20200919_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_name',
            field=models.ForeignKey(default='No user selected', on_delete=django.db.models.deletion.CASCADE, to='todo_list.user'),
        ),
    ]
