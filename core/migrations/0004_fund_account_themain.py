# Generated by Django 3.2.3 on 2021-08-22 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210811_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund_account',
            name='themain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.themain'),
        ),
    ]