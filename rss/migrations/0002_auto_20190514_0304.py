# Generated by Django 2.2 on 2019-05-14 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
