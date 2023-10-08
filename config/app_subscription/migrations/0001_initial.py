# Generated by Django 4.2.6 on 2023-10-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('fullname', models.CharField(max_length=200)),
                ('expire_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
