from django.db import models


class AnimalType(models.Model):
    """
    Class for AnimalType model.
    An AnimalType indicates the species of the animal.
    """

    name = models.CharField("Animal type", max_length=255)
    scientific_name = models.CharField("Scientific name", max_length=255)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    modification_date = models.DateTimeField("Modification date", auto_now=True)

    class Meta:
        verbose_name = "Animal type"
        verbose_name_plural = "Animal types"


class AdoptionStatus(models.Model):
    """
    Class for AdoptionStatus model.
    Indicates the adoption status of an Animal
    """

    status = models.CharField("Status", max_length=255)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    modification_date = models.DateTimeField("Modification date", auto_now=True)

    class Meta:
        verbose_name = "Adoption status"
        verbose_name_plural = "Adoption statuses"


class Animal(models.Model):
    """
    Class for Animal model.
    Is related to every single animal stored.
    """

    name = models.CharField("Name", max_length=255)
    breed = models.CharField("Breed", max_length=255)
    age = models.IntegerField("Age", default=0)
    animal_type = models.ForeignKey(
        AnimalType,
        verbose_name="Animal type",
        on_delete=models.CASCADE,
        related_name="animals",
    )
    adoption_status = models.ForeignKey(
        AdoptionStatus,
        verbose_name="Adoption status",
        on_delete=models.CASCADE,
        related_name="animals",
    )

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"
