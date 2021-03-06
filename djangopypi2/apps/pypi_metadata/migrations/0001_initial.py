# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Architecture',
            fields=[
                ('key', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'architecture',
                'verbose_name_plural': 'architectures',
            },
        ),
        migrations.CreateModel(
            name='Classifier',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'classifier',
                'verbose_name_plural': 'classifiers',
            },
        ),
        migrations.CreateModel(
            name='DistributionType',
            fields=[
                ('key', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'distribution type',
                'verbose_name_plural': 'distribution types',
            },
        ),
        migrations.CreateModel(
            name='PlatformName',
            fields=[
                ('key', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'platform name',
                'verbose_name_plural': 'platform names',
            },
        ),
        migrations.CreateModel(
            name='PythonVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
            ],
            options={
                'ordering': ('major', 'minor'),
                'verbose_name': 'python version',
                'verbose_name_plural': 'python versions',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pythonversion',
            unique_together=set([('major', 'minor')]),
        ),
    ]
