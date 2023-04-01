from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from apps.advertising.models import Advertising


class AdvertisingSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Advertising
        fields = "__all__"

    def create(self, validated_data):
        if validated_data.get('image'):
            image = validated_data.pop('image')
        else:
            image = ''

        return Advertising.objects.create(image=image, **validated_data)


class TemplateSerializer(serializers.Serializer):
    user_pnfl = serializers.CharField(allow_null=True)
