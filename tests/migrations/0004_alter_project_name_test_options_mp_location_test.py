# Generated by Django 5.0 on 2023-12-17 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0003_alter_client_name_test_client_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project_name_test",
            options={"ordering": ["recipient"]},
        ),
        migrations.CreateModel(
            name="Mp_location_test",
            fields=[
                ("transaction", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.CharField(max_length=8)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("created", models.DateTimeField(auto_now=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tests.project_name_test",
                    ),
                ),
            ],
        ),
    ]