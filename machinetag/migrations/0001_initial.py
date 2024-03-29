# Generated by Django 2.2 on 2019-04-09 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, default='', max_length=100)),
                ('predicate', models.CharField(blank=True, default='', max_length=100)),
                ('value', models.CharField(blank=True, default='', max_length=300)),
                ('label', models.CharField(blank=True, default='', max_length=600)),
            ],
            options={
                'verbose_name': 'Machine tag',
                'verbose_name_plural': 'Machine tags',
            },
        ),
        migrations.CreateModel(
            name='MachineTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machinetag_machinetaggeditem_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machinetag_machinetaggeditem_items', to='machinetag.MachineTag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
