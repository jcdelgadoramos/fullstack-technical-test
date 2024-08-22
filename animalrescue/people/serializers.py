from rest_framework import serializers

from people.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model User
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_active"]
