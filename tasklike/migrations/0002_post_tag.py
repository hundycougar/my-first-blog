# Generated by Django 2.1.4 on 2018-12-12 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasklike', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
