# Generated by Django 3.1.1 on 2020-09-18 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20200919_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
