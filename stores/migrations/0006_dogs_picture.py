# Generated by Django 2.0.5 on 2018-05-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_auto_20180510_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='picture',
            field=models.ImageField(blank=True, upload_to='dog_pictures'),
        ),
    ]