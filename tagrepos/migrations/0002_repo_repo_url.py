# Generated by Django 2.1 on 2019-02-24 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tagrepos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='repo_url',
            field=models.URLField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]