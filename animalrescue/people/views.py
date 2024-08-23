from django.contrib.auth.models import Group

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from animalrescue.constants import ADOPTANT_GROUP_NAME, VOLUNTEER_GROUP_NAME
from people.serializers import AdoptantSerializer, VolunteerSerializer


class AdoptantViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model User (only those belonging to Adoptant group)
    """

    adoptant_group = Group.objects.get(name=ADOPTANT_GROUP_NAME)
    queryset = adoptant_group.user_set.all()
    serializer_class = AdoptantSerializer

    def get_permissions(self):
        """
        Sets AllowAny to allow account creation
        and restrict others to Volunteers
        """

        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class VolunteerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for model User (only those belonging to Volunteer group)
    """

    volunteer_group = Group.objects.get(name=VOLUNTEER_GROUP_NAME)
    queryset = volunteer_group.user_set.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAdminUser]
