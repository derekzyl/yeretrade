# Generated by Django 3.2.3 on 2021-08-22 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_fund_account_themain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund_account',
            name='themain',
        ),
    ]
