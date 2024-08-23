from django.contrib.auth.models import Group

from rest_framework import viewsets

from animalrescue.constants import ADOPTANT_GROUP_NAME, VOLUNTEER_GROUP_NAME
from people.serializers import AdoptantSerializer, VolunteerSerializer


class AdoptantViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model User (only those belonging to Adoptant group)
    """

    adoptant_group = Group.objects.get(name=ADOPTANT_GROUP_NAME)
    queryset = adoptant_group.user_set.all()
    serializer_class = AdoptantSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model User (only those belonging to Volunteer group)
    """

    volunteer_group = Group.objects.get(name=VOLUNTEER_GROUP_NAME)
    queryset = volunteer_group.user_set.all()
    serializer_class = VolunteerSerializer
