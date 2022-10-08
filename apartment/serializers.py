from rest_framework import serializers
from apartment.models import Apartment, Floor
from drf_extra_fields.fields import Base64ImageField


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        depth = 1
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        depth = 1
        fields = '__all__'


class MyImageModelSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    image_2d = Base64ImageField()
    image_3d = Base64ImageField()

    class Meta:
        model = Apartment
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image')
        image_2d = validated_data.pop('image_2d')
        image_3d = validated_data.pop('image_3d')

        return Apartment.objects.create(image=image, image_2d=image_2d, image_3d=image_3d, **validated_data)
