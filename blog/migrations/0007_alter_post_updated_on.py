# Generated by Django 3.2.3 on 2021-07-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateField(),
        ),
    ]