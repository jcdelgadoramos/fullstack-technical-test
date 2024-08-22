from rest_framework import viewsets

from animals.models import AdoptionStatus, Animal, AnimalType
from animals.serializers import (
    AdoptionStatusSerializer,
    AnimalSerializer,
    AnimalTypeSerializer,
)


class AdoptionStatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model AdoptionStatus
    """

    queryset = AdoptionStatus.objects.all()
    serializer_class = AdoptionStatusSerializer


class AnimalTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model AnimalType
    """

    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model Animal
    """

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
