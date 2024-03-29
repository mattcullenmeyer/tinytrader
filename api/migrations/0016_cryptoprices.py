# Generated by Django 3.1.7 on 2022-02-22 04:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_delete_cryptoprices'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoPrices',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.FloatField()),
                ('uid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.crypto')),
            ],
        ),
    ]
