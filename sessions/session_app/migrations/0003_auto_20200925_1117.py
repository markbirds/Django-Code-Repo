# Generated by Django 3.1.1 on 2020-09-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_app', '0002_auto_20200925_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]