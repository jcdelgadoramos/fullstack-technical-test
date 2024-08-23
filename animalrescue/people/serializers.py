from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

from animalrescue.constants import ADOPTANT_GROUP_NAME, VOLUNTEER_GROUP_NAME


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model User
    """

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "is_active"]


class AdoptantSerializer(UserSerializer):
    """
    Specific serializer for Adoptants
    """

    def create(self, validated_data):
        group_id = Group.objects.get(name=ADOPTANT_GROUP_NAME).id
        validated_data["groups"] = [group_id,]
        validated_data["username"] = validated_data["email"]
        return super().create(validated_data)


class VolunteerSerializer(UserSerializer):
    """
    Specific serializer for Volunteer 
    """

    def create(self, validated_data):
        group_id = Group.objects.get(name=VOLUNTEER_GROUP_NAME).id
        validated_data["groups"] = [group_id,]
        validated_data["username"] = validated_data["email"]
        validated_data["is_staff"] = True
        return super().create(validated_data)
