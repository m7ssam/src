# Generated by Django 5.0 on 2023-12-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="project_name_test",
            fields=[
                (
                    "recipient",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("project_name", models.CharField(max_length=50)),
                ("client_name", models.CharField(max_length=50)),
            ],
        ),
    ]