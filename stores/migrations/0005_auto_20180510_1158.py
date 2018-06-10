# Generated by Django 2.0.5 on 2018-05-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20180510_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='account',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alluser',
            name='housing_condition',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alluser',
            name='score',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]