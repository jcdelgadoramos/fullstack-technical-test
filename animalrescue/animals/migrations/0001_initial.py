# Generated by Django 5.1 on 2024-08-21 21:04

import django.db.models.deletion
from django.db import migrations, models
from animals.models import AdoptionStatus, AnimalType


def create_adoption_statuses(apps, schema_editor):
    """
    This migration creates the basic adoption statuses
    """
    AdoptionStatus.objects.bulk_create(
        [
            AdoptionStatus(status="Not adopted"),
            AdoptionStatus(status="Adopted"),
            AdoptionStatus(status="In process"),
        ]
    )


def create_animal_types(apps, schema_editor):
    """
    This migration creates the basic animal types
    """
    AnimalType.objects.bulk_create(
        [
            AnimalType(name="Dog", scientific_name="Canis lupus familiaris"),
            AnimalType(name="Cat", scientific_name="Felix silvestris catus"),
        ]
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdoptionStatus",
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
                ("status", models.CharField(max_length=255, verbose_name="Status")),
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
                "verbose_name": "Adoption status",
                "verbose_name_plural": "Adoption statuses",
            },
        ),
        migrations.CreateModel(
            name="AnimalType",
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
                ("name", models.CharField(max_length=255, verbose_name="Animal type")),
                (
                    "scientific_name",
                    models.CharField(max_length=255, verbose_name="Scientific name"),
                ),
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
                "verbose_name": "Animal type",
                "verbose_name_plural": "Animal types",
            },
        ),
        migrations.CreateModel(
            name="Animal",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                ("breed", models.CharField(max_length=255, verbose_name="Breed")),
                ("age", models.IntegerField(default=0, verbose_name="Age")),
                (
                    "adoption_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="animals",
                        to="animals.adoptionstatus",
                        verbose_name="Adoption status",
                    ),
                ),
                (
                    "animal_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="animals",
                        to="animals.animaltype",
                        verbose_name="Animal type",
                    ),
                ),
            ],
            options={
                "verbose_name": "Animal",
                "verbose_name_plural": "Animals",
            },
        ),
        migrations.RunPython(create_adoption_statuses, migrations.RunPython.noop),
        migrations.RunPython(create_animal_types, migrations.RunPython.noop),
    ]
