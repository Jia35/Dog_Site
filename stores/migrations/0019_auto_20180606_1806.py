# Generated by Django 2.0.5 on 2018-06-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0018_alluser_introduce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='introduce',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
