from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from animalrescue.constants import ADOPTANT_GROUP_NAME, VOLUNTEER_GROUP_NAME
from people.serializers import (
    AdoptantSerializer,
    SignInSerializer,
    VolunteerSerializer,
)


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


class SignInView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        received_json_data=request.data
        serializer = SignInSerializer(data=received_json_data)
        if serializer.is_valid():
            user = authenticate(
                request, 
                username=received_json_data["username"], 
                password=received_json_data["password"])
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "id": user.id,
                    "email": user.email,
                    "fullName": f"{user.first_name} {user.last_name}"
                }, status=200)
            else:
                return JsonResponse({
                    "message": "invalid username or password",
                }, status=403)
        else:
            return JsonResponse({"message":serializer.errors}, status=400)
