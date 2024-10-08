from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from animals.models import AdoptionStatus, Animal, AnimalType
from animals.serializers import (
    AdoptionStatusSerializer,
    AnimalSerializer,
    AnimalTypeSerializer,
)


class AdoptionStatusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for model AdoptionStatus
    """

    queryset = AdoptionStatus.objects.all()
    serializer_class = AdoptionStatusSerializer


class AnimalTypeViewSet(viewsets.ReadOnlyModelViewSet):
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

    def get_permissions(self):
        """
        Sets AllowAny for list and retrieve views
        and restrict others to Volunteers
        """

        permission_classes = [AllowAny]
        if self.action not in ["retrieve", "list"]:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
