from rest_framework import serializers
from apps.apartment.models import Apartment, Floor
from drf_extra_fields.fields import Base64ImageField


class ApartmentSerializer(serializers.ModelSerializer):
    roomQuantity = serializers.CharField(source='room_quantity')
    diningRoom = serializers.CharField(source='dining_room')
    livingRoom = serializers.CharField(source='living_room')

    def save(self, **kwargs):
        result = super(ApartmentSerializer, self).save(**kwargs)
        return result

    def validate_area(self, value):
        if value < 0:
            raise serializers.ValidationError("Area can't be negative")
        return value

    class Meta:
        model = Apartment
        write_only_fields = ('is_deleted',)
        depth = 1
        fields = ['id', 'roomQuantity', 'area', 'floor', 'price', 'balcony', 'bedroom', 'bathroom', 'hall', 'kitchen',
                  'diningRoom', 'livingRoom', 'image', 'image_2d', 'image_3d', 'is_deleted']


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        depth = 1
        fields = '__all__'


class MyImageModelSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    image_2d = Base64ImageField(required=False)
    image_3d = Base64ImageField(required=False)
    roomQuantity = serializers.IntegerField(source='room_quantity')

    class Meta:
        model = Apartment
        write_only_fields = ('is_deleted',)
        fields = ['id', 'roomQuantity', 'area', 'floor', 'price', 'balcony', 'bedroom', 'bathroom', 'hall', 'kitchen',
                  'dining_room', 'living_room', 'image', 'image_2d', 'image_3d', 'is_deleted']

    def create(self, validated_data):
        if validated_data.get("image"):
            image = validated_data.pop('image')
        else:
            image = ''
        if validated_data.get("image_2d"):
            image_2d = validated_data.pop('image_2d')
        else:
            image_2d = ''
        if validated_data.get("image_3d"):
            image_3d = validated_data.pop('image_3d')
        else:
            image_3d = ''

        return Apartment.objects.create(image=image, image_2d=image_2d, image_3d=image_3d, **validated_data)
