# Generated by Django 2.0.3 on 2018-04-04 14:38

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jakejieblog', '0005_auto_20180404_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='博客正文'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jakejieblog.Tag', verbose_name='标签'),
        ),
    ]
