# Generated by Django 5.0.4 on 2024-06-07 01:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cliente", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="client",
            name="sobrenome",
        ),
    ]