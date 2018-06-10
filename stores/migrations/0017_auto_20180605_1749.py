# Generated by Django 2.0.5 on 2018-06-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0016_message_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='favorite_food',
            field=models.CharField(default='高麗菜', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dogs',
            name='size',
            field=models.DecimalField(decimal_places=0, default=55, max_digits=3),
            preserve_default=False,
        ),
    ]
