# Generated by Django 3.1.1 on 2020-09-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawform',
            name='programmer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rawform',
            name='language',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
