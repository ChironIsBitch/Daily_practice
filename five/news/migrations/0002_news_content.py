# Generated by Django 2.1.5 on 2019-01-26 00:59

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=DjangoUeditor.models.UEditorField(default=1, verbose_name='文章内容'),
            preserve_default=False,
        ),
    ]
