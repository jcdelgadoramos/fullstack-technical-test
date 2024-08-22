from rest_framework import viewsets

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model Animal
    """

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
