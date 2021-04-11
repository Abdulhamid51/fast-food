# Generated by Django 3.1.5 on 2021-03-04 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood_app', '0002_auto_20210304_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeorder',
            old_name='guass',
            new_name='guast',
        ),
        migrations.AddField(
            model_name='placeorder',
            name='time_to',
            field=models.CharField(default=django.utils.timezone.now, max_length=6, verbose_name='Gacha'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='placeorder',
            name='time_from',
            field=models.CharField(max_length=6, verbose_name='Dan'),
        ),
    ]
