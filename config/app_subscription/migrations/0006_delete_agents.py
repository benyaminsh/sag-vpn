# Generated by Django 4.2.6 on 2023-10-10 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_subscription', '0005_agents'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agents',
        ),
    ]