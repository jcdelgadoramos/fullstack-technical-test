from rest_framework import serializers

from animals.models import AdoptionStatus, AnimalType, Animal


class AdoptionStatusSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model AdoptionStatus
    """

    class Meta:
        model = AdoptionStatus
        fields = ["status"]


class AnimalTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model AnimalType
    """

    class Meta:
        model = AnimalType
        fields = ["name"]


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for model Animal
    """

    class Meta:
        model = Animal
        fields = ["name", "breed", "age", "animal_type", "adoption_status"]
