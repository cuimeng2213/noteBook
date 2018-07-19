# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-17 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者名字')),
                ('address', models.CharField(max_length=32, verbose_name='地址')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('email', models.EmailField(max_length=254, verbose_name='作者邮箱')),
                ('authorinfo', models.TextField(verbose_name='作者简介')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='书名')),
                ('publish_year', models.DateField(verbose_name='出版年份')),
                ('publish_add', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('stocks', models.IntegerField(verbose_name='库存')),
                ('status', models.BooleanField(default=True, verbose_name='出版状态')),
                ('author', models.ManyToManyField(to='managebook.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=32, verbose_name='章节')),
                ('pages', models.IntegerField(verbose_name='页数')),
                ('words', models.IntegerField(verbose_name='字数')),
                ('contentinfo', models.TextField(verbose_name='内容简介')),
                ('logo', models.ImageField(upload_to='', verbose_name='图标')),
                ('catalog', models.TextField(verbose_name='目录')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社名字')),
                ('address', models.CharField(max_length=32, verbose_name='出版社地址')),
            ],
        ),
        migrations.CreateModel(
            name='TypeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_book', models.CharField(max_length=32, verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='managebook.Details'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managebook.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managebook.TypeBook'),
        ),
    ]