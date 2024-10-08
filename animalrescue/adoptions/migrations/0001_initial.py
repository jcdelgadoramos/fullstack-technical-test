# Generated by Django 5.1 on 2024-08-21 21:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from adoptions.models import AdoptionState


def create_adoption_states(apps, schema_editor):
    """
    This migration creates the six adoption states.
    """

    AdoptionState.objects.bulk_create(
        [
            AdoptionState(state="Started"),
            AdoptionState(state="In process"),
            AdoptionState(state="Accepted"),
            AdoptionState(state="Completed"),
            AdoptionState(state="Rejected"),
            AdoptionState(state="Cancelled"),
        ]
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("animals", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AdoptionState",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state", models.CharField(max_length=255, verbose_name="State")),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "modification_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Modification date"
                    ),
                ),
            ],
            options={
                "verbose_name": "Adoption state",
                "verbose_name_plural": "Adoption states",
            },
        ),
        migrations.CreateModel(
            name="Adoption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "adoption_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Adoption date"
                    ),
                ),
                (
                    "adoptant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="adoptions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Adoptant",
                    ),
                ),
                (
                    "animal",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animals.animal",
                        verbose_name="Animal",
                    ),
                ),
                (
                    "volunteer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="adoptions_registered",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Volunteer",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="adoptions",
                        to="adoptions.adoptionstate",
                        verbose_name="State",
                    ),
                ),
            ],
        ),
        migrations.RunPython(create_adoption_states, migrations.RunPython.noop),
    ]
