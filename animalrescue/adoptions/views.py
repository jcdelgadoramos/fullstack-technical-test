from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from adoptions.models import Adoption, AdoptionState
from adoptions.serializers import AdoptionSerializer, AdoptionStateSerializer


class AdoptionStateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for model AdoptionState
    """

    queryset = AdoptionState.objects.all()
    serializer_class = AdoptionStateSerializer


class AdoptionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model Adoption
    """

    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
    permission_classes = [IsAuthenticated]
