# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_popular', models.CharField(max_length=120, verbose_name='Nome popular')),
                ('nome_cientifico', models.CharField(max_length=120, verbose_name='Nome cientifíco')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('fonte', models.CharField(max_length=120, verbose_name='Fonte')),
                ('responsavel', models.CharField(max_length=120, verbose_name='Responsável')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem')),
            ],
        ),
    ]
