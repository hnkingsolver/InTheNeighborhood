# Generated by Django 3.0.8 on 2020-09-02 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itn', '0014_petitions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Petitions',
            new_name='Petition',
        ),
    ]