# Generated by Django 3.2.3 on 2021-05-31 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210531_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.industry'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='last_updated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='liquidity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.liquidity'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='market_cap_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.marketcapsize'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sector'),
        ),
    ]
