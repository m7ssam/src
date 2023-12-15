# Generated by Django 5.0 on 2023-12-15 12:38

import django.db.models.deletion
import manpower.models
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("home", "0001_initial"),
        ("plan", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "contract",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job_type",
            fields=[
                (
                    "title",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Title_list",
            fields=[
                (
                    "title",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Code",
            fields=[
                (
                    "mp_code",
                    models.CharField(max_length=7, primary_key=True, serialize=False),
                ),
                ("job", models.CharField(max_length=50)),
                ("speciality", models.CharField(default="عام", max_length=50)),
                (
                    "calc",
                    models.CharField(
                        choices=[("direct", "direct"), ("indirect", "indirect")],
                        max_length=10,
                    ),
                ),
                (
                    "dep",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.department",
                    ),
                ),
                (
                    "job_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manpower.job_type",
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manpower.title_list",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalMp_list",
            fields=[
                ("id", models.CharField(db_index=True, max_length=8)),
                ("first_name", models.CharField(max_length=20)),
                ("middle_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("full_name", models.CharField(blank=True, max_length=100, null=True)),
                ("full_discription", models.TextField(blank=True, null=True)),
                ("hire", models.DateField()),
                ("birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")], max_length=10
                    ),
                ),
                ("national_id", models.BigIntegerField()),
                (
                    "photo",
                    models.TextField(
                        default="static\\images\\default\\worker.jpg", max_length=100
                    ),
                ),
                ("created", models.DateTimeField(blank=True, editable=False)),
                ("update", models.DateTimeField(blank=True, editable=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "code",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="manpower.code",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="manpower.contract",
                    ),
                ),
                (
                    "gov",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="home.governorate",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical mp_list",
                "verbose_name_plural": "historical mp_lists",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalMp_Location",
            fields=[
                ("id", models.CharField(db_index=True, max_length=8)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="plan.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical mp_ location",
                "verbose_name_plural": "historical mp_ locations",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Mp_list",
            fields=[
                (
                    "id",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("middle_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("full_name", models.CharField(blank=True, max_length=100, null=True)),
                ("full_discription", models.TextField(blank=True, null=True)),
                ("hire", models.DateField()),
                ("birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")], max_length=10
                    ),
                ),
                ("national_id", models.BigIntegerField()),
                (
                    "photo",
                    models.ImageField(
                        default="static\\images\\default\\worker.jpg",
                        upload_to=manpower.models.upload_path,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="manpower.code"
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manpower.contract",
                    ),
                ),
                (
                    "gov",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.governorate",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Mp_Location",
            fields=[
                (
                    "id",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plan.project"
                    ),
                ),
            ],
        ),
    ]