# Generated by Django 4.2 on 2023-05-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_user_description_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='CltNovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_uid', models.CharField(max_length=16, verbose_name='用户id')),
                ('c_tid', models.CharField(max_length=16, verbose_name='帖子id')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
