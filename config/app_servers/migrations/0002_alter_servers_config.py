# Generated by Django 4.2.6 on 2023-10-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='config',
            field=models.TextField(unique=True),
        ),
    ]