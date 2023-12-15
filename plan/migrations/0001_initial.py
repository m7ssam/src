# Generated by Django 5.0 on 2023-12-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "recipient",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("project_name", models.CharField(max_length=50)),
                (
                    "photo",
                    models.ImageField(
                        default="static\\images\\default\\project.jpg",
                        upload_to="project/%Y/%m/%d/",
                    ),
                ),
            ],
        ),
    ]