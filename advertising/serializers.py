from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from advertising.models import Advertising


class AdvertisingSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Advertising
        fields = "__all__"

    def create(self, validated_data):
        image = validated_data.pop('image')

        return Advertising.objects.create(image=image, **validated_data)


