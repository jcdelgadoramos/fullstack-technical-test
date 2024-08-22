from rest_framework import viewsets

from adoptions.models import Adoption 
from adoptions.serializers import AdoptionSerializer


class AdoptionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model Adoption 
    """

    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
