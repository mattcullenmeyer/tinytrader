# Generated by Django 3.2.3 on 2021-05-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_metadata_beta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric',
            name='composite_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='finance_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='mom_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='profit_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='quality_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='safety_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='value_rank',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='vol_rank',
        ),
        migrations.AddField(
            model_name='metadata',
            name='composite_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='finance_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='mom_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='profit_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='quality_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='safety_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='value_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='vol_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
