# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab_access', '0007_auto_20171020_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='professor_responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_access.Professor'),
        ),
    ]
