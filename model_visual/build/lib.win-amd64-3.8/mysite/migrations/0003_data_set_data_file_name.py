# Generated by Django 3.2.2 on 2021-05-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_data_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_set',
            name='data_file_name',
            field=models.CharField(default='', max_length=100, verbose_name='数据文件名'),
        ),
    ]
