# Generated by Django 2.0.5 on 2018-06-14 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0032_auto_20180614_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keym',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.Alluser'),
        ),
    ]
