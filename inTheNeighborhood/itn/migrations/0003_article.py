# Generated by Django 3.0.8 on 2020-08-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itn', '0002_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
