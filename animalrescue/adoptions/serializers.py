from rest_framework import serializers

from adoptions.models import AdoptionState, Adoption


class AdoptionStateSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model AdoptionState
    """

    class Meta:
        model = AdoptionState
        fields = ["state"]


class AdoptionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model Adoption
    """

    class Meta:
        model = Adoption
        fields = ["animal", "adoptant", "volunteer", "adoption_date", "state"]
