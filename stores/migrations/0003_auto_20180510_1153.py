# Generated by Django 2.0.5 on 2018-05-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20180510_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=1, default=3, max_digits=3),
        ),
    ]
