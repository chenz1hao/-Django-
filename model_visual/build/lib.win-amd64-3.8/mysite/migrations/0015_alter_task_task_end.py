# Generated by Django 3.2.2 on 2021-05-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_auto_20210519_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_end',
            field=models.DateTimeField(default=None, verbose_name='结束时间'),
        ),
    ]