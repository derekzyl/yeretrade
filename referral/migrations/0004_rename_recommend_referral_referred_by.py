# Generated by Django 3.2.3 on 2021-08-22 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0003_alter_referral_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='recommend',
            new_name='referred_by',
        ),
    ]