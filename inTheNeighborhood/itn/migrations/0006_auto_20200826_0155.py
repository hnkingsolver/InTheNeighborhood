# Generated by Django 3.0.8 on 2020-08-26 01:55

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('itn', '0005_contact'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contact',
            managers=[
                ('ojects', django.db.models.manager.Manager()),
            ],
        ),
    ]
