# Generated by Django 2.0.5 on 2018-06-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0014_alluser_chat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='nickname',
        ),
        migrations.AddField(
            model_name='message',
            name='account',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alluser',
            name='account',
            field=models.CharField(max_length=30),
        ),
    ]
