from django.db import models

from animals.models import Animal
from people.models import User


class AdoptionState(models.Model):
    """
    Class for AdoptionState
    Sets the state for the adoption
    """

    state = models.CharField("State", max_length=255)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    modification_date = models.DateTimeField("Modification date", auto_now=True)

    class Meta:
        verbose_name = "Adoption state"
        verbose_name_plural = "Adoption states"


class Adoption(models.Model):
    """
    Class for Adoption
    Stores information for an adoption of an Animal by an Adoptant
    """

    animal = models.OneToOneField(
        Animal,
        verbose_name="Animal",
        on_delete=models.CASCADE,
    )
    adoptant = models.ForeignKey(
        User,
        verbose_name="Adoptant",
        on_delete=models.CASCADE,
        related_name="adoptions",
    )
    volunteer = models.ForeignKey(
        User,
        verbose_name="Volunteer",
        on_delete=models.CASCADE,
        related_name="adoptions_registered",
    )
    adoption_date = models.DateTimeField("Adoption date", auto_now_add=True)
    state = models.ForeignKey(
        AdoptionState,
        verbose_name="State",
        on_delete=models.CASCADE,
        related_name="adoptions",
    )
