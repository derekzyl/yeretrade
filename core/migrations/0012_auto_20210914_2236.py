# Generated by Django 3.2.3 on 2021-09-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210901_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund_account',
            name='fund_id',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='invest',
            name='invest_id',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
