# Generated by Django 5.0.4 on 2024-04-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fulltexto", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fulltexto",
            name="texto_original",
            field=models.TextField(blank=True, null=True),
        ),
    ]