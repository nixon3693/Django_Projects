# Generated by Django 4.0.3 on 2023-07-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SyslogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('datetime', models.CharField(max_length=50)),
                ('host', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=200)),
                ('alert', models.TextField()),
            ],
        ),
    ]