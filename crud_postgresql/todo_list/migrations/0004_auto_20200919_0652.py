# Generated by Django 3.1.1 on 2020-09-18 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20200918_2107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
