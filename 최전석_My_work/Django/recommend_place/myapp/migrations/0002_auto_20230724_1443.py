# Generated by Django 3.2.18 on 2023-07-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='age',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='companion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='gender',
            field=models.CharField(max_length=200),
        ),
    ]
