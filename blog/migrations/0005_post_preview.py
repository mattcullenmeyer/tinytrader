# Generated by Django 3.2.3 on 2021-07-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
