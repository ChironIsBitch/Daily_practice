# Generated by Django 2.1.3 on 2019-01-24 23:56

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
            ],
        ),
    ]
