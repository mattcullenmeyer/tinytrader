# Generated by Django 3.1.7 on 2022-02-23 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_crypto_cryptoprices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='crypto',
            name='status',
        ),
    ]