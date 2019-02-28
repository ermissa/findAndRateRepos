# Generated by Django 2.1 on 2019-02-27 23:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tagrepos', '0005_auto_20190226_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='long_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repository',
            name='short_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]