# Generated by Django 3.2.7 on 2021-10-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
