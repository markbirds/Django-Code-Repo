# Generated by Django 3.1.1 on 2020-09-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_forms', '0003_auto_20200913_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawform',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='rawform',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='rawform',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Favorite Programming language'),
        ),
        migrations.AlterField(
            model_name='rawform',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
