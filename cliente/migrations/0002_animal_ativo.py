# Generated by Django 5.0.4 on 2024-06-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
